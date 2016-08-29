from cornice import Service
import json
import yaml

convert_json_yaml_service = Service(
    name='convert_json_yaml_service',
    path='/json/yaml',
    description="Convert JSON to YAML"
)

@convert_json_yaml_service.post(renderer='string')
def get_convert_json_yaml_service(request):
    json_str = json.loads(request.body)
    return yaml.safe_dump(json_str)