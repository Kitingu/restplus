from flask_restplus import Namespace, Resource, fields
from restApi.models.users import User
from restApi.helpers.user_helper import UserParser
import jwt
from instance.config import Config
from werkzeug.security import check_password_hash, generate_password_hash
# from flask_jwt_extended import create_access_token, jwt_required,get_raw_jwt,JWTManager
from flask import request, jsonify
import datetime
from .auth import token_required

blacklist = set()
User_object = User()
user_api = Namespace("Users", description="")
new_user = user_api.model('Users', {'email': fields.String('email@example.com'),
                                    'username': fields.String('test_user'),
                                    'password': fields.String('test_pass'),
                                    'confirm_password': fields.String('test_pass')

                                    })
user_login = user_api.model('Login', {'email': fields.String('email@example.com'),
                                      'password': fields.String('test_pass')})


class Users(Resource):
    # @token_required
    def get(self):
        response = User_object.get_all_users()
        return response, 200

    @user_api.expect(new_user)
    def post(self):
        data = UserParser.parser.parse_args()
        hashed_pass = generate_password_hash(data['password'])
        new_user = User_object.get_single_user(data['email'])
        for items in data.values():
            if items == "":
                return "Fields must not be blank"
            if new_user:
                return "user with email: {} already exists".format(data["email"]), 400
            if check_password_hash(hashed_pass, data['confirm_password']):
                User_object.create_user(data['email'], data['username'], hashed_pass)
                return "User registered successfully", 201
            return "passwords do not match", 401


class LogIn(Resource):
    @user_api.expect(user_login)
    def post(self):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        data = UserParser.parser.parse_args()
        email = str(data['email'])
        password = str(data['password'])
        for items in data.values():
            if items == "":
                return "Fields must not be blank"
            if email in User_object.users:
                if check_password_hash(User_object.users[email]['password'], password):
                    access_token = jwt.encode({"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},Config.SECRET)
                    return {"access_token": access_token.decode('utf-8')}, 200
                return {"msg": "Invalid email or password"}, 401
            return "user does not exist", 400


# class LogOut(Resource):
#     @token_required
#     def post(self):
#         jti = get_raw_jwt()['jti']
#         blacklist.add(jti)
#         return {"msg": "Successfully logged out"}, 200


user_api.add_resource(Users, '/users')
user_api.add_resource(LogIn, '/users/login')
# user_api.add_resource(LogOut, '/users/logout')
