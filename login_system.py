def login_system():
    users = {
        "admin": "1234",
        "user1": "pass1",
        "user2": "pass2"
    }

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful! ✅")
    else:
        print("Invalid username or password ❌")

login_system()