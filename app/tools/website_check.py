from app.utils.tool import Tool
import urllib, re

class WebsiteCheck(Tool):
    def __init__(self):
        self.description = """Sometimes websites don't appear online from
            where you are. This tool is to check website availability from
            our server's perspective."""
        self.placeholder.append("(e.g. http://www.onlinecodinghelper.com)")

    def execute(self, **kwargs):
        http_code = ''
        try:
            url = kwargs['one']
            if re.match('(?:http|https)://', url) is None:
                return 'URL format is incorrect. Please follow e.g. http://www.onlinecodinghelper.com'
            http_code = urllib.urlopen(url).getcode()
        except Exception, e:
            return str(e)

        return 'Website is online' if http_code == 200 else 'Website is unavailable'