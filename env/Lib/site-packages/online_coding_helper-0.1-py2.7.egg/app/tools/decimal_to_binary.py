from app.utils.tool import Tool

class DecimalToBinary(Tool):
    def execute(self, **kwargs):
        return bin(int(kwargs['one'])).split('b')[1]