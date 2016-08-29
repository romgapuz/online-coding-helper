from app.utils.tool import Tool

class BinaryToOctal(Tool):
    def execute(self, **kwargs):
        return oct(int(kwargs['one'], 2))