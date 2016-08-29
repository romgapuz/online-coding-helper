from app.utils.tool import Tool
import hmac

class Hmac(Tool):
    def __init__(self):
        self.title = "HMAC"
        self.label.append("Shared Secret Key")
        self.label.append("Data")

    def execute(self, **kwargs):
        h = hmac.new(kwargs['one'])
        h.update(kwargs['two'])
        return h.hexdigest()