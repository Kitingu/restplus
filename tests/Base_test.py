import os, sys
import unittest
from restApi.app import create_app
from restApi.models.rides import Rides
from restApi.models.users import User
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RideObject=Rides()
UserObject=User()

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.test_ride = {
            "start_point": "Nairobi",
            "destination": "Kiambu",
            "seats_available": 5,
            "date": "12/02/2018",
            "time": "10:25"
        }
        self.edit_ride = {
            "start_point": "Nairobi",
            "destination": "Kiambu",
            "seats_available": 5,
            "date": "12/02/2028",
            "time": "10:28"
        }
        self.invalid_ride = {
            "start_point": "Nairobi",
            "destination": "Kiambu",
            "seats_available": 5,
            "date": "",
            "time": ""
        }
        self.test_user = {
            "email": "asdf@gmail.com",
            "username": "test_user",
            "password": "test_pass",
            "confirm_password": "test_pass"
        }
        self.login_user = {
            "email": "kasee@gmail.com",
            "username": "test_user",
            "password": "test_pass",
            "confirm_password": "test_pass"
        }
        self.test_user1 = {
            "email": "gathee@gmail.com",
            "username": "test_user",
            "password": "test_pass",
            "confirm_password": "test_pass"
        }
        self.invalid_user = {
            "email": "@gmail.com",
            "username": "",
            "password": "test_pass",
            "confirm_password": "test_pass"
        }
        self.test_user2 = {
            "email": "blah@gmail.com",
            "username": "test_user",
            "password": "test_pass",
            "confirm_password": "test_pass"
        }
        self.test_request = {
            "email": "ben@gmail.com",
            "username": "bene",
            "number_of_seats": 5,
            "pick_up_point": "ikinu",
            "destination": "Githunguri"
        }

        self.request_many = {
            "email": "ben@gmail.com",
            "username": "bene",
            "number_of_seats": 9,
            "pick_up_point": "ikinu",
            "destination": "Githunguri"
        }
        self.test_login = {
            "email": "kasee@gmail.com",
            "password": "test_pass",
        }

        self.test_login2 = {
            "email": "maskoff@gmail.com",
            "password": "test_pass",
        }
        self.invalid_login = {
            "email": "gathee@gmail.com",
            "password": "test_pss",
        }
        self.approve = {
            "approval": "true"}
        self.decline = {
            "approval": "false"}

        user_response=self.client().post('/api/v1/users', data=json.dumps(self.login_user), content_type='application/json')
        user_login=self.client().post('/api/v1/users/login', data=json.dumps(self.test_login),
                                      content_type='application/json')
        user_token = json.loads(user_login.get_data(as_text=True))
        token = user_token['access_token']
        self.user_header = {"Content-Type": "application/json", "x-access-token": token}
    def tearDown(self):

        RideObject.rides.clear()
        RideObject.requests.clear()
        UserObject.users.clear()




