from tests.Base_test import BaseTest
import json


class TestLogin(BaseTest):
    def test_login(self):
        resp = self.client().post('/api/v1/users', data=json.dumps(self.login_user), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        response = self.client().post('/api/v1/users/login', data=json.dumps(self.test_login),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_non_registered(self):
        resp = self.client().post('/api/v1/users/login', data=json.dumps(self.test_login2),
                                  content_type='application/json')
        self.assertEqual(resp.status_code, 400)
        response_msg = json.loads(resp.data.decode("UTF-8"))
        self.assertIn(response_msg, "user does not exist")
