from cornice import Service
from csscompressor import compress

minify_css_service = Service(
    name='minify_css_service',
    path='/cssminify',
    description="Minify css"
)

@minify_css_service.post(renderer='string')
def get_minify_css_service(request):
    return compress(request.body)