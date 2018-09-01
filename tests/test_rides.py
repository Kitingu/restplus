import os,sys
import json
from tests.base import BaseTest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestRides(BaseTest):
    """This is a class to test the functionality of the rides routes"""

    def test_create_ride(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_with_invalid_input(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.invalid_ride),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_create_with_non_json(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.invalid_ride),
                                      content_type='application/text')
        self.assertEqual(response.status_code, 400)


