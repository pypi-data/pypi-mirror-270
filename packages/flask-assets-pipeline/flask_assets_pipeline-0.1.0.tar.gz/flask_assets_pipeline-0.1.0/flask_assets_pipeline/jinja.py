from jinja2.ext import Extension
from jinja2.lexer import count_newlines
from jinja2.lexer import Token
from jinja2.exceptions import TemplateSyntaxError
from jinja2.compiler import CodeGenerator as BaseCodeGenerator
from jinja2 import nodes
from flask import current_app
import re
import os


# We want our asset_tags directive to print tags once all code has been executed,
# to make sure include_asset can be called from anywhere (even from includes)
#
# To achieve this, we use a combination of a custom Environment.concat, an override to CodeGenerator and an extension.
#
# 1. The extension first replaces the {% asset_tags %} directive with an ExtensionAttribute node.
# 2. In our CodeGenerator override, we catch calls to this node and ensure that an unescaped yield statement is used.
# 3. The AssetTagsExtension.asset_tags property returns an object that will be evaluated only when converted to string
#    (when the template is finally concatanated all together which is the last step).
# 4. Our custom Envrionment.concat will ensure that the result from the CodeGenerator is first transformed to list
#    so the generator expression is fully evaluated, then converts all items to strings and finally joins them together.
#
# Note that they are drawbacks to this approach as streaming is not possible anymore


def configure_environment(env, inline_assets=False):
    env.concat = env_concat
    env.code_generator_class = CodeGenerator
    env.add_extension(AssetTagsExtension)
    if inline_assets:
        env.add_extension(InlineScriptExtension)
        env.add_extension(InlineStyleExtension)


def env_concat(items):
    return "".join(map(str, list(items)))


class CodeGenerator(BaseCodeGenerator):
    def visit_Output(self, node, frame):
        if isinstance(node.nodes[0], nodes.ExtensionAttribute) and node.nodes[0].identifier == "flask_frontend.jinja.AssetTagsExtension":
            # do not escape the output
            self.writeline("yield ")
            self.visit_ExtensionAttribute(node.nodes[0], frame)
        else:
            super().visit_Output(node, frame)


class AssetTagsStr:
    def __str__(self):
        return current_app.extensions["frontend"].instance.tags()


class AssetTagsExtension(Extension):
    tags = ["asset_tags"]

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return nodes.Output([self.attr("asset_tags")], lineno=lineno)
    
    @property
    def asset_tags(self):
        return AssetTagsStr()


class InlineAssetExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        if not hasattr(self, "open_tag_re"):
            self.open_tag_re = re.compile(r'<\s*%s\s+bundle(="([^"]+)")?\s*>' % self.tags[0])
        if not hasattr(self, "close_tag_re"):
            self.close_tag_re = re.compile(r"</\s*%s\s*>" % self.tags[0])

    def filter_stream(self, stream):
        out = []
        for token in stream:
            if token.type != "data":
                out.append(token)
                continue

            lineno = token.lineno

            open_match = self.open_tag_re.search(token.value)
            if open_match is None:
                out.append(token)
                continue

            try:
                filename = open_match.group(2)
            except IndexError:
                filename = None

            if not filename:
                filename = f"{os.path.relpath(stream.filename, current_app.root_path)}.{self.fileext}"

            if open_match.start() > 0:
                preval = token.value[:open_match.start()]
                out.append(Token(lineno, "data", preval))
                lineno += count_newlines(preval)

            end_match = self.close_tag_re.search(token.value)
            if not end_match:
                raise TemplateSyntaxError(
                    f"unclosed {self.tags[0]} tag",
                    token.lineno,
                    stream.name,
                    stream.filename,
                )
            
            content = token.value[open_match.end():end_match.start()]
            block_end_lineno = lineno + count_newlines(content)
            out.extend([
                Token(lineno, "block_begin", None),
                Token(lineno, "name", self.tags[0]),
                Token(lineno, "const", filename),
                Token(lineno, "block_end", None),
                Token(lineno, "data", content),
                Token(block_end_lineno, "block_begin", None),
                Token(block_end_lineno, "name", f"end{self.tags[0]}"),
                Token(block_end_lineno, "block_end", None)
            ])
            
            if end_match.end() < len(token.value):
                out.append(Token(block_end_lineno, "data", token.value[end_match.end():]))

        return out
        
    def parse(self, parser):
        lineno = next(parser.stream).lineno
        filename = next(parser.stream).value
        body = parser.parse_statements([f"name:end{self.tags[0]}"], drop_needle=True)
        content = body[0].nodes[0].data
        state = current_app.extensions["frontend"]
        if getattr(self.environment, "write_inline_assets", None):
            pathname = os.path.join(state.assets_folder, filename)
            os.makedirs(os.path.dirname(pathname), exist_ok=True)
            with open(pathname, "w") as f:
                f.write(content)
        state.bundles[filename] = [filename]
        return nodes.Output([nodes.Call(nodes.Name("include_asset", "load"), [nodes.Const(filename)], [], None, None, lineno=lineno)])
    

class InlineScriptExtension(InlineAssetExtension):
    tags = ["script"]
    fileext = "js"


class InlineStyleExtension(InlineAssetExtension):
    tags = ["style"]
    fileext = "css"
