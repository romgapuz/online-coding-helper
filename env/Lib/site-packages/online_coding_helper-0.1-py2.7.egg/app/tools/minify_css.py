from app.utils.tool import Tool
from csscompressor import compress

class MinifyCss(Tool):
    def __init__(self):
        self.title = "Minify CSS"
        self.description = """This tool removes unnecessary characters in your CSS code
            to reduce size (in bytes) which therefore greatly increase webpage load times.
            The trade-off is unreadable code."""

    def execute(self, **kwargs):
        return compress(kwargs['one'])