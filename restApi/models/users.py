import uuid


class User:
    users = {}

    def __init__(self):
        ...

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

    def delete_user(self, email):
        del self.users[email]

    def update_user(self, email, username, password, confirm_password):
        self.users[email] = {
            "username": username,
            "password": password,
            "confirm_password": confirm_password}
