import os, sys
import unittest
from restApi.app import create_app

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
            "number_of_seats": 5000,
            "pick_up_point": "ikinu",
            "destination": "Githunguri"
        }

    def tearDown(self):
        del self.edit_ride
        del self.invalid_ride
        del self.test_ride
        del self.test_user
        del self.test_user2


if __name__ == '__main__':
    unittest.main()
