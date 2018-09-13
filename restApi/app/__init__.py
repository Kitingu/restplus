from flask import Flask, request, jsonify
from flask_restplus import Api
from flask_jwt_extended import JWTManager

from instance.config import app_config


def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=True)
    app.config['JWT_SECRET_KEY'] = 'this is secret'
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.config['JWT_TOKEN_LOCATION'] = ['headers']

    jwt = JWTManager(app)
    jwt.init_app(app)
    api = Api(app=app, description="This is a carpooling api designed using flask RESTplus",
              title="Ride my way",
              version="1",
              license="MIT",
              contact_email='benedictmwendwa47@gmail.com')

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    from restApi.resources.rides import ride_api
    api.add_namespace(ride_api, path='/api/v1')
    from restApi.resources.requests import request_api
    api.add_namespace(request_api, path='/api/v1')
    from restApi.resources.users import user_api
    api.add_namespace(user_api, path='/api/v1')
    return app
