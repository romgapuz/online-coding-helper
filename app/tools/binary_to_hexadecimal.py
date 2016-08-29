from app.utils.tool import Tool

class BinaryToHexadecimal(Tool):
    def execute(self, **kwargs):
        return hex(int(kwargs['one'], 2)).split('x')[1]