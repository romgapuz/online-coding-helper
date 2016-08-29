from app.utils.tool import Tool
import urllib2

class UrlDecode(Tool):
    def __init__(self):
        self.title = "URL Decode"
        self.description = """Uniform Resource Locator (URL), or web address, is an
            address/reference to a web resource. Only ASCII characters are allowed in URLs,
            other characters can be included provided it is "encoded". This tool help
            decode urls to original format."""

    def execute(self, **kwargs):
        return urllib2.unquote(kwargs['one']).decode('utf8')