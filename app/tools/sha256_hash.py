from app.utils.tool import Tool
import hashlib

class Sha256Hash(Tool):
    def execute(self, **kwargs):
        return hashlib.sha256(kwargs['one']).hexdigest()