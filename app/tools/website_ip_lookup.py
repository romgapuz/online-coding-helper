from app.utils.tool import Tool
import socket

class WebsiteIpLookup(Tool):
    def __init__(self):
        self.title = "Website IP Lookup"
        self.placeholder.append("(e.g. www.onlinecodinghelper.com)")

    def execute(self, **kwargs):
        ip = ''
        try:
            ip = socket.gethostbyname(kwargs['one'])
        except Exception, e:
            return 'Host not available or invalid'

        return ip