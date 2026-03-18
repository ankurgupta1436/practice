class AuthSystem:
    def __init__(self):
        self.users = {}  # username: password

    def register(self, username, password):
        if username in self.users:
            return "User already exists"
        self.users[username] = password
        return "Registration successful"

    def login(self, username, password):
        if username not in self.users:
            return "User not found"
        if self.users[username] == password:
            return "Login successful"
        return "Invalid password"


# Example usage
auth = AuthSystem()
print(auth.register("admin", "1234"))
print(auth.login("admin", "1234"))