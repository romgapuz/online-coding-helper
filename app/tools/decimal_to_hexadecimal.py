from app.utils.tool import Tool

class DecimalToHexadecimal(Tool):
    def execute(self, **kwargs):
        return hex(int(kwargs['one'])).split('x')[1]