from cornice import Service
import json
import yaml

convert_yaml_json_service = Service(
    name='convert_yaml_json_service',
    path='/yaml/json',
    description="Convert YAML to JSON"
)

@convert_yaml_json_service.post(renderer='string')
def get_convert_yaml_json_service(request):
    yaml_str = yaml.load(request.body)
    return json.dumps(
    	yaml_str,
		indent=2,
		separators=(',', ': ')
	)