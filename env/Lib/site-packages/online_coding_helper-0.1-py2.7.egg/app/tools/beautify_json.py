from app.utils.tool import Tool
import json

class BeautifyJson(Tool):
    def __init__(self):
        self.title = "Beautify JSON"

    def execute(self, **kwargs):
        json_str = json.load(kwargs['one'])
        return json.dumps(
            json_str,
            indent=2,
            separators=(',', ': ')
        )