import json
from .Base_test import BaseTest


class DeclineApproval(BaseTest):
    def test_decline(self):
        response = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        resp = self.client().post('/api/v1/rides/1/requests', data=json.dumps(self.test_request),
                                  content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        resp = self.client().post('/api/v1/requests/1', data=json.dumps(self.decline), content_type='application/json')
        self.assertEqual(resp.status_code, 401)









