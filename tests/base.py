import os,sys
import unittest
from restApi.app import create_app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BaseTest(unittest.TestCase):
    def setUp(self):

        self.app=create_app("testing")
        self.client=self.app.test_client
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
    def tearDown(self):
        del self.edit_ride
        del self.invalid_ride
        del self.test_ride

if __name__ == '__main__':
    unittest.main()