import json

from tests.Base_test import BaseTest


class TestUser(BaseTest):


    def test_token_generation(self):
        """test if JWT tokens are generated"""

        response = self.client().post('/api/v1/users/login', data=json.dumps(self.test_user),
                                      content_type='application/json')
        self.assertEqual(response.status_code,200)