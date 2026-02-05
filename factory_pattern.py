class User:
    def __init__(self, role):
        self.role = role

    def get_permissions(self):
        return []


class Admin(User):
    def get_permissions(self):
        return ["read", "write", "delete"]



class Guest(User):
    def get_permissions(self):
        return ["read"]


class UserFactory:
    @staticmethod
    def create_user(role):
        if role == "admin":
            return Admin(role)
        if role == "guest":
            return Guest(role)
        raise ValueError("Unknown role")


user = UserFactory.create_user("admin")
print(user.get_permissions())
