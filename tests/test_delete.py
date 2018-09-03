import sys, os
import json
from tests.base import BaseTest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDelete(BaseTest):
    """This is a class to test the functionality of the rides routes"""

    def test_delete_ride(self):
        rv = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        response = self.client().delete('/api/v1/rides/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_non_existing(self):
        response = self.client().delete('/api/v1/rides/1')
        self.assertEqual(response.status_code, 404)
