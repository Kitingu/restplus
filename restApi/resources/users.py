from flask_restplus import Namespace, Resource, fields
from restApi.models.users import User
from restApi.helpers.user_helper import UserParser
from werkzeug.security import check_password_hash,generate_password_hash

User_object = User()
user_api = Namespace("Users", description="")
new_user = user_api.model('Users', {'email': fields.String('email@example.com'),
                                    'username': fields.String('test_user'),
                                    'password': fields.String('test_pass'),
                                    'confirm_password': fields.String('test_pass')

                                    })


class Users(Resource):
    def get(self):
        response = User_object.get_all_users()
        return response

    @user_api.expect(new_user)
    def post(self):
        data = UserParser.parser.parse_args()
        hashed_pass=generate_password_hash(data['password'])
        if check_password_hash(hashed_pass,data['confirm_password']):
            User_object.create_user(data['email'], data['username'], hashed_pass)
            return "User registered successfully", 201
        return "passwords do not match"

    def put(self):
        ...




user_api.add_resource(Users, '/users')
