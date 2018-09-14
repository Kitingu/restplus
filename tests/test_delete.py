import sys, os
import json
from tests.Base_test import BaseTest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDelete(BaseTest):
    """This is a class to test that rides can be deleted"""

    def test_delete_ride(self):
        rv = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride), content_type='application/json',headers=self.user_header)
        self.assertEqual(rv.status_code, 201)
        response = self.client().delete('/api/v1/rides/1',headers=self.user_header)
        self.assertEqual(response.status_code, 200)


    def test_delete_non_existing(self):
        """this is a test to test a ride that does not exist"""
        response = self.client().delete('/api/v1/rides/1',headers=self.user_header)
        self.assertEqual(response.status_code, 404)
