from app.utils.tool import Tool

class DecimalToOctal(Tool):
    def execute(self, **kwargs):
        return oct(int(kwargs['one']))