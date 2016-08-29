from app.utils.tool import Tool
import json
import yaml

class JsonToYaml(Tool):
    def execute(self, **kwargs):
        json_str = json.loads(kwargs['one'])
        return yaml.safe_dump(json_str)