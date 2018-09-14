import sys,os
import json
import unittest
from tests.Base_test import BaseTest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
class TestRides(BaseTest):
    """This is a class to test the functionality of the rides routes"""

    def test_create_ride(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride),
                                      content_type='application/json',headers=self.user_header)
        self.assertEqual(response.status_code, 201)

    def test_create_with_invalid_input(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.invalid_ride),
                                      content_type='application/json',headers=self.user_header)
        self.assertEqual(response.status_code, 400)

    def test_create_with_non_json(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.invalid_ride),
                                      content_type='application/text',headers=self.user_header)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()