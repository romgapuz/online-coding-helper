from app.utils.tool import Tool
import zlib

class Crc32(Tool):
    def execute(self, **kwargs):
            return zlib.crc32(kwargs['one'])