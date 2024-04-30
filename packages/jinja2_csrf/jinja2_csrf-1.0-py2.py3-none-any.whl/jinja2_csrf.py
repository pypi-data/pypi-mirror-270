from jinja2 import nodes
from jinja2.ext import Extension


class CSRFTokenExtension(Extension):
    tags = {"csrf_token"}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return nodes.Output(
            [
                nodes.MarkSafe(
                    nodes.Const(
                        '<input type="hidden" name="csrfmiddlewaretoken" value="'
                    )
                ),
                nodes.Getitem(
                    nodes.ContextReference(), nodes.Const("csrf_token"), "load"
                ),
                nodes.MarkSafe(nodes.Const('">')),
            ]
        ).set_lineno(lineno)
