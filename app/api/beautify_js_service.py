from cornice import Service
import jsbeautifier
import slimit

beautify_js_service = Service(
    name='beautify_js_service',
    path='/jsbeautify',
    description="Beautify javascript"
)

@beautify_js_service.post(renderer='string')
def get_beautify_js_service(request):
    opts = jsbeautifier.default_options()
    opts.indent_size = 4

    return jsbeautifier.beautify(request.body, opts)

minify_js_service = Service(
    name='minify_js_service',
    path='/jsminify',
    description="Minify javascript"
)

@minify_js_service.post(renderer='string')
def get_minify_js_service(request):
    return slimit.minify(request.body)