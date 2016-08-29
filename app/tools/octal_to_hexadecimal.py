from app.utils.tool import Tool

class OctalToHexadecimal(Tool):
    def execute(self, **kwargs):
        return hex(int(kwargs['one'], 8)).split('x')[1]