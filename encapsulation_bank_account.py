class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)


acc = BankAccount("Amit", 10000)
acc.deposit(2000)
acc.withdraw(5000)
acc.show_balance()