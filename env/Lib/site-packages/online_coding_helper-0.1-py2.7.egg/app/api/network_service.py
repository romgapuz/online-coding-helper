from cornice import Service
import socket
import urllib

dns_lookup_service = Service(
    name='dns_lookup_service',
    path='/dnslookup',
    description="DNS lookup"
)

@dns_lookup_service.post(renderer='string')
def get_dns_lookup_service(request):
    ip = ''
    try:
        ip = socket.gethostbyname(request.body)
    except Exception, e:
        return 'Host not available or invalid'

    return ip

website_check_service = Service(
    name='website_check_service',
    path='/websitecheck',
    description="Check if website is up"
)

@website_check_service.post(renderer='string')
def get_website_check_service(request):
    http_code = ''
    try:
        http_code = urllib.urlopen(request.body).getcode()
    except Exception, e:
        return str(e)

    return http_code == 200

port_check_service = Service(
    name='port_check_service',
    path='/portcheck',
    description="Check if port is open"
)

@port_check_service.post(renderer='string')
def get_port_check_service(request):
    url = request.body
    pos = url.rfind(':')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((url[:pos], int(url[pos+1:])))

    return result == 0