import re

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def length_ok(self):
        return len(self.password) >= 8

    def has_upper(self):
        return bool(re.search(r"[A-Z]", self.password))

    def has_lower(self):
        return bool(re.search(r"[a-z]", self.password))

    def has_digit(self):
        return bool(re.search(r"\d", self.password))

    def has_special(self):
        return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password))

    def score(self):
        checks = [
            self.length_ok(),
            self.has_upper(),
            self.has_lower(),
            self.has_digit(),
            self.has_special()
        ]
        return sum(checks)

    def strength(self):
        score = self.score()
        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Medium"
        return "Strong"

def main():
    password = input("Enter password: ")
    checker = PasswordChecker(password)

    print(f"Password strength: {checker.strength()}")
    print(f"Score: {checker.score()}/5")

if __name__ == "__main__":
    main()
