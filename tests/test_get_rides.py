import sys,os
from tests.Base_test import BaseTest
import json
class Test_get_rides(BaseTest):

    def test_get_all_rides(self):
        """Test if user can be able to fetch all the available rides"""
        resp = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 201)
        response = self.client().get('/api/v1/rides',headers=self.user_header)
        self.assertEqual(response.status_code, 200)

    def test_get_single_ride(self):
        """Tests that user can fetch a single ride"""
        resp = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 201)
        response = self.client().get('/api/v1/rides/1',headers=self.user_header)
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing(self):
        response = self.client().get('/api/v1/rides/1588')
        self.assertEqual(response.status_code, 404)

