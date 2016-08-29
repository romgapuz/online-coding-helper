from cornice import Service

convert_hex_dec_service = Service(
    name='convert_hex_dec_service',
    path='/hex/dec',
    description="Convert hexadecimal to decimal"
)

@convert_hex_dec_service.post(renderer='string')
def get_convert_hex_dec_service(request):
    return int(request.body, 16)

convert_hex_bin_service = Service(
    name='convert_hex_bin_service',
    path='/hex/bin',
    description="Convert hexadecimal to binary"
)

@convert_hex_bin_service.post(renderer='string')
def get_convert_hex_bin_service(request):
    return bin(int(request.body, 16)).split('b')[1]

convert_hex_oct_service = Service(
    name='convert_hex_oct_service',
    path='/hex/oct',
    description="Convert hexadecimal to octal"
)

@convert_hex_oct_service.post(renderer='string')
def get_convert_hex_oct_service(request):
    return oct(int(request.body, 16))