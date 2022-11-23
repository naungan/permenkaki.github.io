from wsgiref.simple_server import make_server
from pyramid.config import Configurator


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('readjson', '/json')
        config.add_route('readxml', '/xml')
        config.add_route('readcsv', '/csv')
        config.include('pyramid_jinja2')
        config.scan('views')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print("server start")
    print("boot OK")
    server.serve_forever()
    