import json

from tests.Base_test import BaseTest


class TestUserUpdate(BaseTest):

    def test_user_update(self):
        resp = self.client().post('/api/v1/users', data=json.dumps(self.test_user2), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        resp = self.client().put('/api/v1/users/asdf@gmail.com', data=json.dumps(self.test_user1),
                                 content_type='application/json',headers=self.user_header)
        self.assertEqual(resp.status_code, 200)