class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        print("Deposit successful.")
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("Current Balance:", self.balance)

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Deposit: "))

        if acc_no in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[acc_no] = BankAccount(acc_no, name, balance)
            print("Account created successfully.")

    def access_account(self):
        acc_no = input("Enter Account Number: ")

        if acc_no not in self.accounts:
            print("Account not found.")
            return

        account = self.accounts[acc_no]

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Select option: ")

            if choice == "1":
                amount = float(input("Enter amount: "))
                account.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter amount: "))
                account.withdraw(amount)

            elif choice == "3":
                account.show_balance()

            elif choice == "4":
                break

            else:
                print("Invalid choice")


def main():
    bank = BankSystem()

    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            bank.access_account()

        elif choice == "3":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid option")


main()