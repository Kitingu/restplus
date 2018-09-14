import json
from tests.Base_test import BaseTest


class Request(BaseTest):

    def test_get_requests(self):
        response = self.client().get('api/v1/requests',headers=self.user_header)
        self.assertEqual(response.status_code, 200)

    def test_create_request(self):
        resp = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 201)
        resp = self.client().post('/api/v1/rides/1/requests', data=json.dumps(self.test_request),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 201)

    def test_request_non_existing(self):
        resp = self.client().post('/api/v1/rides/888/requests', data=json.dumps(self.test_request),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 404)

    def test_request_more_than_available_seats(self):
        resp = self.client().post('/api/v1/rides', data=json.dumps(self.test_ride),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 201)
        resp = self.client().post('/api/v1/rides/1/requests', data=json.dumps(self.request_many),
                                  content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 400)
