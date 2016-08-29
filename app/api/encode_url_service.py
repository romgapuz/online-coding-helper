from cornice import Service
import urllib2

encode_url_service = Service(
    name='encode_url_service',
    path='/urlencode',
    description="Url encode"
)

@encode_url_service.post(renderer='string')
def get_encode(request):
    return urllib2.quote(request.body)

decode_url_service = Service(
    name='decode_url_service',
    path='/urldecode',
    description="Url decode"
)

@decode_url_service.post(renderer='string')
def get_decode(request):
    return urllib2.unquote(request.body).decode('utf8')
