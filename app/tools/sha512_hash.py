from app.utils.tool import Tool
import hashlib

class Sha512Hash(Tool):
    def execute(self, **kwargs):
        return hashlib.sha512(kwargs['one']).hexdigest()