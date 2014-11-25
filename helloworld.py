# coding: utf-8
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.i18n import TranslationStringFactory
_ = TranslationStringFactory('dom')


def hello_world(request):
    ts = _('Add')
    localizer = request.localizer
    translated = localizer.translate(ts)
    return Response('%s %s!' % (translated, request.matchdict['name']))

if __name__ == '__main__':
    config = Configurator(settings={'pyramid.default_locale_name': 'de'})
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    # config.add_translation_dirs('locale', 'locale_override')
    ## -> Addieren (override)
    
    # config.add_translation_dirs('locale_override', 'locale')
    ## -> Hinzufügen (non-override)
    
    config.add_translation_dirs('locale_override')
    config.add_translation_dirs('locale')
    ## -> Addieren (override)
    
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8123, app)
    server.serve_forever()
