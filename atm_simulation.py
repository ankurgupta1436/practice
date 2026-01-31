# ATM Simulation System

balance = 5000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Current Balance: ₹{balance}")

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance and amount > 0:
            balance -= amount
            print("Please collect your cash.")
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == 4:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice.")
