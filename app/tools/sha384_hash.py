from app.utils.tool import Tool
import hashlib

class Sha384Hash(Tool):
    def execute(self, **kwargs):
        return hashlib.sha384(kwargs['one']).hexdigest()