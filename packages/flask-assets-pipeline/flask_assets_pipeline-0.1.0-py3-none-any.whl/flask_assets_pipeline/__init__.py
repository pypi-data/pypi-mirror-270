from flask import render_template, g, has_request_context, url_for, send_from_directory
from markupsafe import Markup
from dataclasses import dataclass
import typing as t
import os
import json
import subprocess
import re
from .cli import assets_cli
from .jinja import configure_environment
from .livereload import LIVERELOAD_SCRIPT
from .utils import copy_files, copy_assets


@dataclass
class FlaskAssetsPipelineState:
    bundles : t.Sequence[str] | t.Mapping[str, t.Sequence[str]]
    include : t.Sequence[str]
    route_template : str
    inline : bool
    import_map : t.Mapping[str, str]
    expose_node_packages : t.Sequence[str]
    assets_folder : str
    assets_endpoint: str
    assets_url_path : str
    stamp_assets : bool
    output_folder : str
    output_url : str
    mapping_file : str
    esbuild_cache_metafile : bool
    esbuild_args : t.Sequence[str]
    esbuild_bin : str
    esbuild_splitting : bool
    esbuild_target : t.Optional[t.Sequence[str]]
    livereload_port : str
    tailwind : str
    tailwind_args : t.Sequence[str]
    tailwind_bin : str
    node_modules_path: str
    copy_files_from_node_modules: t.Mapping[str, str]
    cdn_host: str
    cdn_enabled: bool
    mapping: t.Mapping[str, t.Sequence[str]]
    instance: "FlaskAssetsPipeline"


PRELOAD_AS_EXT_MAPPING = {"css": "style", "js": "script", "png": "image", "jpg": "image", "jpeg": "image",
                          "gif": "image", "webp": "image", "svg": "image", "woff": "font",
                          "woff2": "font", "ttf": "font", "otf": "font", "mp4": "video", "webm": "video",
                          "ogg": "video", "mp3": "audio", "wav": "audio", "flac": "audio", "aac": "audio",
                          "json": "fetch", "html": "fetch"}


class FlaskAssetsPipeline:
    def __init__(self, app=None, **kwargs):
        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, bundles=None, include=None, route_template="frontend_route.html", inline=False,
                 import_map=None, expose_node_packages=None, assets_folder=None, assets_url_path="/static/assets", stamp_assets=True,
                 output_folder="static/dist", output_url="/static/dist", mapping_file="assets.json", esbuild_cache_metafile=None,
                 esbuild_args=None, esbuild_bin=["npx", "esbuild"], esbuild_splitting=True, esbuild_target=None, livereload_port="8000",
                 tailwind=None, tailwind_args=None, tailwind_bin=["npx", "tailwindcss"], node_modules_path="node_modules",
                 copy_files_from_node_modules=None, cdn_host=None, cdn_enabled=None):
        
        if assets_folder is None:
            assets_folder = app.static_folder
        else:
            assets_folder = os.path.join(app.root_path, assets_folder)
        if isinstance(bundles, list):
            bundles = {bundle: [bundle] for bundle in bundles}
        if include is None and bundles:
            include = list(bundles.keys())
        
        self.app = app
        state = self.state = FlaskAssetsPipelineState(
            bundles=app.config.get("FRONTEND_BUNDLES", bundles or {}),
            include=app.config.get("FRONTEND_INCLUDE", include or []),
            route_template=app.config.get("FRONTEND_ROUTE_TEMPLATE", route_template),
            inline=app.config.get("FRONTEND_INLINE", inline),
            import_map=app.config.get("FRONTEND_IMPORT_MAP", import_map or {}),
            expose_node_packages=app.config.get("FRONTEND_EXPOSE_NODE_PACKAGES", expose_node_packages or []),
            assets_folder=app.config.get("FRONTEND_ASSETS_FOLDER", assets_folder),
            assets_endpoint="static",
            assets_url_path=app.config.get("FRONTEND_ASSETS_URL_PATH", assets_url_path),
            stamp_assets=app.config.get("FRONTEND_STAMP_ASSETS", stamp_assets),
            output_folder=app.config.get("FRONTEND_OUTPUT_FOLDER", os.path.join(app.root_path, output_folder)),
            output_url=app.config.get("FRONTEND_OUTPUT_URL", output_url),
            mapping_file=app.config.get("FRONTEND_MAPPING_FILE", os.path.join(app.root_path, mapping_file)),
            esbuild_cache_metafile=app.config.get("FRONTEND_ESBUILD_CACHE_METAFILE", not app.debug if esbuild_cache_metafile is None else esbuild_cache_metafile),
            esbuild_args=app.config.get("FRONTEND_ESBUILD_ARGS", esbuild_args or []),
            esbuild_bin=app.config.get("FRONTEND_ESBUILD_BIN", esbuild_bin),
            esbuild_splitting=app.config.get("FRONTEND_ESBUILD_SPLITTING", esbuild_splitting),
            esbuild_target=app.config.get("FRONTEND_ESBUILD_TARGET", esbuild_target),
            livereload_port=app.config.get("FRONTEND_LIVERELOAD_PORT", livereload_port),
            tailwind=app.config.get("FRONTEND_TAILWIND", tailwind),
            tailwind_args=app.config.get("FRONTEND_TAILWIND_ARGS", tailwind_args or []),
            tailwind_bin=app.config.get("FRONTEND_TAILWIND_BIN", tailwind_bin),
            node_modules_path=app.config.get("FRONTEND_NODE_MODULES_PATH", node_modules_path),
            copy_files_from_node_modules=app.config.get("FRONTEND_COPY_FILES_FROM_NODE_MODULES", copy_files_from_node_modules or {}),
            cdn_host=app.config.get("FRONTEND_CDN_HOST", cdn_host),
            cdn_enabled=app.config.get("FRONTEND_CDN_ENABLED", not app.debug if cdn_enabled is None else cdn_enabled),
            mapping={},
            instance=self
        )
        app.extensions["frontend"] = state

        if not state.cdn_host:
            state.cdn_enabled = False

        if app.static_folder != state.assets_folder and app.debug:
            # in debug mode, no need to copy assets to static, we serve them directly
            app.add_url_rule(
                f"{state.assets_url_path}/<path:filename>",
                endpoint="assets",
                view_func=lambda filename: send_from_directory(state.assets_folder,
                                                               filename, max_age=app.get_send_file_max_age(filename))
            )
            state.assets_endpoint = "assets"

        self.map_exposed_node_packages()
        configure_environment(app.jinja_env, inline_assets=state.inline)

        state.mapping = self.read_mapping()
        if not app.debug and (state.bundles or state.tailwind or app.static_folder != state.assets_folder) and not state.mapping:
            app.logger.warning("No assets mapping found, please run 'flask assets build' to generate it")

        @app.before_request
        def before_request():
            g.include_assets = list(state.include)
            if state.tailwind:
                g.include_assets.append(f"{state.output_url}/{state.tailwind}")

        def include_asset(*args, **kwargs):
            self.include(*args, **kwargs)
            return ""

        app.jinja_env.globals.update(
            include_asset=include_asset,
            asset_url=self.url,
            static_url=lambda f, **kw: url_for("static", filename=f, **kw)
        )

        app.cli.add_command(assets_cli)

    def read_mapping(self):
        try:
            with open(self.state.mapping_file, "r") as f:
                return json.load(f)
        except:
            return {}

    def include(self, path):
        if has_request_context():
            g.include_assets.append(path)
        else:
            self.state.include.append(path)
    
    def resolve(self, filename):
        if has_request_context() and "assets_map" in g:
            mapping = g.assets_map
        else:
            mapping = self.state.mapping
            if self.app.debug:
                mapping = self.read_mapping()
            if has_request_context():
                g.assets_map = mapping
        return mapping.get(filename, [filename])
    
    def url(self, filename, with_type=False, single=True, external=False):
        filenames = []
        r = re.compile("(import|prefetch|preload( as [a-z]+)?) ")
        for url in self.resolve(filename):
            m = r.match(url)
            type = None
            if m:
                type = m.group(1)
                url = url[m.end():]
            if not re.match("[a-z]+://", url):
                if not url.startswith("/"):
                    url = url_for(self.state.assets_endpoint, filename=url, _external=external if not self.state.cdn_enabled else False)
                if self.state.cdn_enabled:
                    url = self.state.cdn_host + url
            filenames.append((type, url) if with_type else url)
        return filenames[0] if single else filenames

    def urls(self, paths=None, with_type=False):
        if paths is None:
            paths = g.include_assets if has_request_context() else self.state.include
        out = []
        for f in paths:
            out.extend(self.url(f, with_type, False))
        return out

    def tags(self):
        tags = []
        if self.state.import_map:
            tags.append('<script type="importmap">%s</script>' % json.dumps({"imports": self.state.import_map}))
        for type, url in self.urls(with_type=True):
            if type == "prefetch":
                tags.append('<link rel="prefetch" href="%s">' % url[9:])
            elif type.startswith("preload"):
                if type.startswith("preload as "):
                    as_attr = type.split(" as ")[1]
                else:
                    as_attr = PRELOAD_AS_EXT_MAPPING.get(url.split(".")[-1], "fetch")
                tags.append('<link rel="preload" href="%s" as="%s">' % (url, as_attr))
            elif type == "import":
                tags.append('<script src="%s" type="module"></script>' % url[7:])
            elif url.endswith(".css"):
                tags.append('<link rel="stylesheet" href="%s">' % url)
            else:
                tags.append('<script src="%s"></script>' % url)
        if self.app.debug:
            tags.append(LIVERELOAD_SCRIPT % {"livereload_port": self.state.livereload_port})
        return Markup("\n".join(tags))

    def add_route(self, endpoint, url, decorators=None, **options):
        view_func = lambda: render_template(self.route_template)
        if decorators:
            for decorator in decorators:
                view_func = decorator(view_func)
        self.app.add_url_rule(url, endpoint=endpoint, view_func=view_func, **options)

    def map_import(self, name, url):
        self.state.import_map[name] = url

    def extract_from_templates(self, env=None, loader=None, write=True):
        if not env:
            env = self.app.jinja_env
        if not loader:
            loader = env.loader
        with self.app.app_context():
            env.write_inline_assets = write
            for template in loader.list_templates():
                env.get_template(template)

    def copy_assets_to_static(self, src=None, dest=None, stamp=None, ignore_files=None):
        if src is None:
            src = self.state.assets_folder
        if dest is None:
            dest = self.app.static_folder
        if stamp is None:
            stamp = self.state.stamp_assets

        ignore_files = ignore_files or []
        for files in self.state.bundles.values():
            ignore_files.extend(files)
        if self.state.tailwind:
            ignore_files.append(self.state.tailwind)

        return copy_assets(src, dest, stamp, ignore_files, self.app.logger)

    def get_bundles_esbuild_command(self, watch=False, dev=False, metafile=None):
        args = []
        for files in self.state.bundles.values():
            args.extend([os.path.join(self.state.assets_folder, f) for f in files])
        args.extend([
            "--bundle",
            "--format=esm",
            "--asset-names=[dir]/[name]-[hash]",
            "--chunk-names=[dir]/[name]-[hash]",
            "--entry-names=[dir]/[name]-[hash]",
            f"--outbase={self.state.assets_folder}",
            f"--outdir={self.state.output_folder}",])
        if self.state.esbuild_splitting:
            args.append("--splitting")
        if self.state.esbuild_target:
            args.append(f"--target={','.join(self.state.esbuild_target)}")
        if metafile:
            args.append(f"--metafile={metafile}")
        if dev:
            args.append("--sourcemap")
        else:
            args.append("--minify")
        if watch:
            args.append("--watch")
        args.extend(self.state.esbuild_args)
        return self.make_esbuild_command(args)
    
    def make_esbuild_command(self, args):
        return self.state.esbuild_bin + args if isinstance(self.state.esbuild_bin, list) else [self.state.esbuild_bin, *args]

    def convert_esbuild_metafile(self, filename=None):
        if not filename:
            filename = self.state.esbuild_metafile
        inputrel = os.path.relpath(self.state.assets_folder) + "/"
        outputrel = os.path.relpath(self.state.output_folder)

        with open(filename) as f:
            meta = json.load(f)

        inputs = []
        for input, info in meta["inputs"].items():
            inputs.append(input[len(inputrel):])

        mapping = {}
        for output, info in meta["outputs"].items():
            if "entryPoint" not in info:
                continue
            o = mapping.setdefault(info["entryPoint"][len(inputrel):], [])
            url = self.state.output_url + output[len(outputrel):]
            if url.endswith(".js"):
                url = f"import {url}"
            o.append(url)
            if "cssBundle" in info:
                o.append(self.state.output_url + info["cssBundle"][len(outputrel):])
            for import_info in info["imports"]:
                if import_info["kind"] == "import-statement":
                    o.append("preload " + self.state.output_url + import_info["path"][len(outputrel):])
        
        return inputs, mapping
    
    def get_tailwind_command(self, watch=False, dev=False):
        input = os.path.join(self.state.assets_folder, self.state.tailwind)
        output = os.path.join(self.state.output_folder, self.state.tailwind)
        args = ["-i", input, "-o", output]
        if not dev:
            args.append("--minify")
        if watch:
            args.append("--watch")
        args.extend(self.state.tailwind_args)
        return self.state.tailwind_bin + args if isinstance(self.state.tailwind_bin, list) else [self.state.tailwind_bin, *args]
    
    def check_tailwind_config(self):
        if not os.path.exists("tailwind.config.js"):
            with open("tailwind.config.js", "w") as f:
                f.write(TAILWIND_CONFIG)
        if not os.path.exists(os.path.join(self.state.assets_folder, self.state.tailwind)):
            with open(os.path.join(self.state.assets_folder, self.state.tailwind), "w") as f:
                f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;")

    def build_node_dependencies(self):
        for pkg in self.state.expose_node_packages:
            self.build_node_package(pkg)
        if self.state.copy_files_from_node_modules:
            self.copy_files_from_node_modules(self.state.copy_files_from_node_modules)

    def map_exposed_node_packages(self):
        for name in self.state.expose_node_packages:
            if ":" in name:
                name, _ = name.split(":", 1)
            self.map_import(name, f"{self.state.output_url}/vendor/{name}.js")

    def build_node_package(self, name):
        if ":" in name:
            name, input = name.split(":", 1)
        else:
            input = f"export * from '{name}'"
        outfile = os.path.join(self.state.output_folder, "vendor", f"{name}.js")
        if not os.path.exists(outfile):
            os.makedirs(os.path.dirname(outfile), exist_ok=True)
            subprocess.run(self.make_esbuild_command(["--bundle", "--minify", "--format=esm", f"--sourcefile={name}.js", f"--outfile={outfile}"]), input=input.encode("utf-8"))
    
    def copy_files_from_node_modules(self, files):
        copy_files(files, self.state.node_modules_path, self.state.output_folder, self.app.logger)


TAILWIND_CONFIG = """
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
"""