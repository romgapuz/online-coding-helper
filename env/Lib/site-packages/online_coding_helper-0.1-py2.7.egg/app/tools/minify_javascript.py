from app.utils.tool import Tool
import slimit

class MinifyJavascript(Tool):
    def __init__(self):
        self.description = """Reduce your javascript code size using this tool to improve
            webpage load times."""

    def execute(self, **kwargs):
        return slimit.minify(kwargs['one'])