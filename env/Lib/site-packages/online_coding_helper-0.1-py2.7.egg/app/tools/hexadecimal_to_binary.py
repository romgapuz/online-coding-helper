from app.utils.tool import Tool

class HexadecimalToBinary(Tool):
    def execute(self, **kwargs):
        return bin(int(kwargs['one'], 16)).split('b')[1]