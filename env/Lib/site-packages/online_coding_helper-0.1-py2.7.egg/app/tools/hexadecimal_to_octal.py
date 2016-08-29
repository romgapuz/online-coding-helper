from app.utils.tool import Tool

class HexadecimalToOctal(Tool):
    def execute(self, **kwargs):
        return oct(int(kwargs['one'], 16))