from flask import Flask
from server import service

from resources.blueprint.blueprint import blueprint as api

application = service.application

application.register_blueprint(api, url_prefix='/redis')
