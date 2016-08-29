from app.utils.tool import Tool
import jsbeautifier

class BeautifyJavascript(Tool):
    def __init__(self):
        self.description = """This is a tool for formatting javascript code to make it
            human-readable."""

    def execute(self, **kwargs):
        opts = jsbeautifier.default_options()
        opts.indent_size = 4

        return jsbeautifier.beautify(kwargs['one'], opts)