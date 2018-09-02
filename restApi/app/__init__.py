# import os
# os.chdir(os.path.dirname(__file__))
from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager

from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['JWT_SECRET_KEY'] = 'this is secret'
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    jwt = JWTManager(app)
    api = Api(app=app, description="This is a carpooling api design using flask restplus",
              title="Ride my way",
              version="1",
              license="MIT",
              contact_email='benedictmwendwa47@gmail.com')

    # client.config.from_object(app_config[config_name])
    # client.config.from_pyfile('config.py')
    def token_required(f):
        """All endoints that need log in will be wrapped by this decorator"""

        @wraps(f)
        def decorated(*args, **kwargs):
            token = None

            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']

            if not token:
                return jsonify({'Message': 'You need to log in'}), 401

            try:
                data = jwt.decode(token, os.getenv('SECRET'))
                if data['username'] in user_object.u_token:
                    current_user = user_object.users[data['username']]
                else:
                    return jsonify({"Message": "Token expired:Login again"}), 401
            except BaseException:
                return jsonify({'Message': 'Invalid request!'}), 401

            return f(current_user, *args, **kwargs)

        return decorated

    @jwt.expired_token_loader
    def my_expired_token_callback():
        return {
                   'status': 401,
                   'sub_status': 42,
                   'msg': 'The token has expired'
               }, 401

    blacklist = set()

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        '''check if token is blacklisted'''
        jti = decrypted_token['jti']
        return jti in blacklist

    from restApi.resources.rides import ride_api
    api.add_namespace(ride_api, path='/api/v1')
    from restApi.resources.requests import request_api
    api.add_namespace(request_api, path='/api/v1')
    from restApi.resources.users import user_api
    api.add_namespace(user_api, path='/api/v1')
    return app
