from app.utils.tool import Tool
import base64

class Base64Decode(Tool):
    def __init__(self):
        self.description = """Base64 is a text-encoding scheme used to encode binary data
            to ASCII string format."""

    def execute(self, **kwargs):
        return base64.b64decode(kwargs['one'])