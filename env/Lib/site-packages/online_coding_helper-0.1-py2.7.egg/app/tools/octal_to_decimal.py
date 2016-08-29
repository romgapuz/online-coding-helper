from app.utils.tool import Tool

class OctalToDecimal(Tool):
    def execute(self, **kwargs):
        return int(kwargs['one'], 8)