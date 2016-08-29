from app.utils.tool import Tool

class HexadecimalToDecimal(Tool):
    def execute(self, **kwargs):
        return int(kwargs['one'], 16)