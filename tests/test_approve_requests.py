import json
from .Base_test import BaseTest


class TestApproval(BaseTest):

    def test_approve_non_existing(self):
        resp = self.client().post('/api/v1/requests/1', data=json.dumps(self.approve), content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code,404 )

    def test_approve(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride),
                                      content_type='application/json',headers=self.user_header)
        self.assertEqual(response.status_code, 201)
        resp = self.client().post('/api/v1/rides/1/requests', data=json.dumps(self.test_request),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 201)
        resp = self.client().post('/api/v1/requests/1', data=json.dumps(self.approve), content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code,202 )



