# import os
# os.chdir(os.path.dirname(__file__))
from flask import Flask
from flask_restplus import Api

from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app=app, description="This is a carpooling api design using flask restplus",
              title="Ride my way",
              version="1",
              license="MIT",
              contact_email='benedictmwandwa47@gmail.com')

    # client.config.from_object(app_config[config_name])
    # client.config.from_pyfile('config.py')
    from restApi.resources.rides import ride_api
    api.add_namespace(ride_api, path='/api/v1')
    from restApi.resources.requests import request_api
    api.add_namespace(request_api, path='/api/v1')
    from restApi.resources.users import user_api
    api.add_namespace(user_api, path='/api/v1')
    return app
