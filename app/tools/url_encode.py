from app.utils.tool import Tool
import urllib2

class UrlEncode(Tool):
    def __init__(self):
        self.title = "URL Encode"
        self.description = """Uniform Resource Locator (URL), or web address, is an
            address/reference to a web resource. Only ASCII characters are allowed in URLs,
            other characters can be included provided it is "encoded". This tool help
            encode urls to proper format."""

    def execute(self, **kwargs):
        return urllib2.quote(kwargs['one'])