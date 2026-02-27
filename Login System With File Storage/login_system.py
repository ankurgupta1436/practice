def register(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("User registered successfully ✅")


def login(username, password):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
    except FileNotFoundError:
        print("No users registered yet.")
    return False


# Example Usage
choice = input("Register (r) or Login (l): ")

if choice == "r":
    u = input("Enter username: ")
    p = input("Enter password: ")
    register(u, p)

elif choice == "l":
    u = input("Enter username: ")
    p = input("Enter password: ")
    if login(u, p):
        print("Login successful ✅")
    else:
        print("Invalid credentials ❌")