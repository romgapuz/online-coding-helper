from app.utils.tool import Tool
import hashlib

class Sha1Hash(Tool):
    def execute(self, **kwargs):
        return hashlib.sha1(kwargs['one']).hexdigest()