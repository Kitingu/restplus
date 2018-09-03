import sys, os
import json
import unittest
from tests.Base_test import BaseTest


class TestUser(BaseTest):

    def test_login(self):
        resp = self.client().post('/api/v1/users', data=json.dumps(self.test_user), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        response = self.client().post('/api/v1/users/login', data=json.dumps(self.test_user),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # def test_token_generation(self):
    #     resp = self.client().post('/api/v1/users', data=json.dumps(self.test_user), content_type='application/json')
    #     self.assertEqual(resp.status_code, 201)
    #     response = self.client().post('/api/v1/users/login', data=json.dumps(self.test_user),
    #                                   content_type='application/json')
    #     self.assertIn(str(response.data), "'access_token'")
