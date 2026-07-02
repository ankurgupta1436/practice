#  Take a password string and check basic rules (length ≥ 8 and contains at least one digit).  

password = input("Enter your password: ")

if len(password) >= 8:
    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if has_digit:
        print("Password is valid.")
    else:
        print("Password must contain at least one digit.")
else:
    print("Password must be at least 8 characters long.")