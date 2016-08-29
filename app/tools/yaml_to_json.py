from app.utils.tool import Tool
import json
import yaml

class YamlToJson(Tool):
    def execute(self, **kwargs):
        yaml_str = yaml.load(kwargs['one'])
        return json.dumps(
            yaml_str,
            indent=2,
            separators=(',', ': ')
        )