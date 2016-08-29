from app.utils.tool import Tool
import urllib

class PortCheck(Tool):
    def execute(self, **kwargs):
        url = kwargs['one']
        pos = url.rfind(':')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((url[:pos], int(url[pos+1:])))

        return result == 0