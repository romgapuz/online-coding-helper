from pyramid.view import view_config
from pyramid.renderers import get_renderer

class DefaultView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(route_name='root', renderer='../templates/index.pt')
    def home_view(self):
        return {
            'home_menu': 'active',
            'about_menu': '',
            'toolbox_menu': ''
        }

    @view_config(route_name='about', renderer='../templates/about.pt')
    def about_view(self):
        return {
            'home_menu': '',
            'about_menu': 'active',
            'toolbox_menu': ''
        }

    @view_config(route_name='toolbox', renderer='../templates/toolbox.pt')
    def toolbox_view(self):
        return {
            'home_menu': '',
            'about_menu': '',
            'toolbox_menu': 'active'
        }