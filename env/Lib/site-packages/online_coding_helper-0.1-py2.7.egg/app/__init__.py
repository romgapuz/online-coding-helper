"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # api
    config.include("cornice")
    config.scan("app.api.encode_base64_service")
    config.scan("app.api.encode_url_service")
    config.scan("app.api.beautify_css_service")
    config.scan("app.api.beautify_js_service")
    config.scan("app.api.convert_json_service")
    config.scan("app.api.convert_yaml_service")
    config.scan("app.api.convert_decimal_service")
    config.scan("app.api.convert_hexadecimal_service")
    config.scan("app.api.convert_binary_service")
    config.scan("app.api.network_service")

    # web
    config.include('pyramid_chameleon')
    config.add_static_view(name='static', path='app.web:static', cache_max_age=3600)
    config.add_route('root', '/')
    config.add_route('about', '/about')
    config.add_route('toolbox', '/toolbox')
    config.add_route('tool', '/toolbox/{tool}')
    config.add_route('tool_2', '/toolbox-2/{tool}')
    config.scan("app.web.views.default")
    config.scan("app.web.views.tool")
    config.scan("app.web.subscribers.master_page")

    return config.make_wsgi_app()
