import sys,os
from .base import  BaseTest
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Test_edit_rides(BaseTest):
    def test_edit_non_existing(self):
        response = self.client().put('/api/v1/rides/1', data=json.dumps(self.edit_ride),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_edit_ride(self):
        rv = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        response = self.client().put('/api/v1/rides/1', data=json.dumps(self.edit_ride),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ride updated successfully', str(response.data))

    def test_edit_with_invalid_details(self):
        rv = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        response = self.client().put('/api/v1/rides/1', data=json.dumps(self.invalid_ride),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)

