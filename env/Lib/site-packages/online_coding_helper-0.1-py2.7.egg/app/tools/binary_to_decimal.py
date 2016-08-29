from app.utils.tool import Tool

class BinaryToDecimal(Tool):
    def execute(self, **kwargs):
        return int(kwargs['one'], 2)