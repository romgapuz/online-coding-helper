from app.utils.tool import Tool
import hashlib

class Md5Hash(Tool):
    def execute(self, **kwargs):
        return hashlib.md5(kwargs['one']).hexdigest()