from asgiref.wsgi import WsgiToAsgi
from pyramid.config import Configurator
from pyramid.response import Response
import os
import subprocess

def config_routes():
    with Configurator() as config:
        config.add_route('index', '/')
        config.add_route('process', '/process')
        config.add_route('download', '/download')
        config.add_static_view(name='assets', path=os.getcwd() + '/templates/assets')
        config.scan('views')
        config.include('pyramid_chameleon')
        return config.make_wsgi_app()

throttle_process = True
if throttle_process:
    subprocess.Popen(["cpulimit", "--exe", "ffmpeg", "--limit=10"])
app = config_routes()
app = WsgiToAsgi(app)