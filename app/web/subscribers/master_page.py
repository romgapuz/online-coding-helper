from pyramid.renderers import get_renderer
from pyramid.interfaces import IBeforeRender
from pyramid.events import subscriber

@subscriber(IBeforeRender)
def globals_factory(event):
    master = get_renderer('../templates/master.pt').implementation()
    event['master'] = master