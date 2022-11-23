
from wsgiref.simple_server import make_server
from pyramid.config import Configurator


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('create', '/create')
        config.add_route('update', '/update')
        config.add_route('delete', '/delete')
        config.include('pyramid_jinja2')
        config.scan('viewcars')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print("cars server start")
    print("boot OK")
    server.serve_forever()