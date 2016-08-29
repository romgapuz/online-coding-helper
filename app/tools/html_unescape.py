from app.utils.tool import Tool
import HTMLParser

class HtmlUnescape(Tool):
    def execute(self, **kwargs):
        h = HTMLParser.HTMLParser()
        return h.unescape(kwargs['one'])