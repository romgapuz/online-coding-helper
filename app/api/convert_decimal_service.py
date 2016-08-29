from cornice import Service

convert_dec_hex_service = Service(
    name='convert_dec_hex_service',
    path='/dec/hex',
    description="Convert decimal to hexadecimal"
)

@convert_dec_hex_service.post(renderer='string')
def get_convert_dec_hex_service(request):
    return hex(int(request.body)).split('x')[1]

convert_dec_oct_service = Service(
    name='convert_dec_oct_service',
    path='/dec/oct',
    description="Convert decimal to octal"
)

@convert_dec_oct_service.post(renderer='string')
def get_convert_dec_oct_service(request):
    return oct(int(request.body))

convert_dec_bin_service = Service(
    name='convert_dec_bin_service',
    path='/dec/bin',
    description="Convert decimal to binary"
)

@convert_dec_bin_service.post(renderer='string')
def get_convert_dec_bin_service(request):
    return bin(int(request.body)).split('b')[1]