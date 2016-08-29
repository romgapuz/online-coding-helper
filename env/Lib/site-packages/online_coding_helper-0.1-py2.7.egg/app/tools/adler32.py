from app.utils.tool import Tool
import zlib

class Adler32(Tool):
    def execute(self, **kwargs):
        return zlib.adler32(kwargs['one'])