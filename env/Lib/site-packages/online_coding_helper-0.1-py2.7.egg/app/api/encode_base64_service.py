from cornice import Service
import base64

encode_base64_service = Service(
    name='encode_base64_service',
    path='/base64encode',
    description="Base64 encode"
)

@encode_base64_service.post(renderer='string')
def get_encode(request):
    return base64.b64encode(request.body)

decode_base64_service = Service(
    name='decode_base64_service',
    path='/base64decode',
    description="Base64 decode"
)

@decode_base64_service.post(renderer='string')
def get_decode(request):
    return base64.b64decode(request.body)
