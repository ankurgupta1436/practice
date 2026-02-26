def login_system():
    correct_username = "admin"
    correct_password = "1234"
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful! ✅")
            return
        else:
            attempts -= 1
            print("Wrong credentials. Attempts left:", attempts)

    print("Account locked! ❌")

login_system()