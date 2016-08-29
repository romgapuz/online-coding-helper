from app.utils.tool import Tool
import hashlib

class Sha224Hash(Tool):
    def execute(self, **kwargs):
        return hashlib.sha224(kwargs['one']).hexdigest()