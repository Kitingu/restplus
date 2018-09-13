import uuid


class User:
    users = {}

    def create_user(self, email, username, password, admin=False):
        self.users[email] = {
            "username": username,
            "password": password,
            "user_id": str(uuid.uuid4()),
            "admin": admin
        }

    def get_single_user(self, email):
        if email in self.users:
            return self.users[email]

    def get_all_users(self):
        return {"users": self.users}

    def update_user(self, email, username, password):
        self.users[email] = {
            "username": username,
            "password": password
        }

