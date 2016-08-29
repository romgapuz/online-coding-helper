from cornice import Service

convert_bin_dec_service = Service(
    name='convert_bin_dec_service',
    path='/bin/dec',
    description="Convert binary to decimal"
)

@convert_bin_dec_service.post(renderer='string')
def get_convert_bin_dec_service(request):
    return int(request.body, 2)

convert_bin_hex_service = Service(
    name='convert_bin_hex_service',
    path='/bin/hex',
    description="Convert binary to hexadecimal"
)

@convert_bin_hex_service.post(renderer='string')
def get_convert_bin_hex_service(request):
    return hex(int(request.body, 2)).split('x')[1]

convert_bin_oct_service = Service(
    name='convert_bin_oct_service',
    path='/bin/oct',
    description="Convert binary to octal"
)

@convert_bin_oct_service.post(renderer='string')
def get_convert_bin_oct_service(request):
    return oct(int(request.body, 2))