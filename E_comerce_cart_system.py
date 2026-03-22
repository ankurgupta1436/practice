# E-commerce Cart System

cart = {}

while True:
    print("\n1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        item = input("Enter item name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if item in cart:
            cart[item]['quantity'] += quantity
        else:
            cart[item] = {'price': price, 'quantity': quantity}

    elif choice == '2':
        print("\n--- Cart ---")
        total = 0
        for item, details in cart.items():
            cost = details['price'] * details['quantity']
            total += cost
            print(item, ":", details['quantity'], "x", details['price'], "=", cost)
        print("Total =", total)

    elif choice == '3':
        item = input("Enter item to remove: ")
        if item in cart:
            del cart[item]
            print("Item removed")
        else:
            print("Item not found")

    elif choice == '4':
        total = 0
        print("\n--- Bill ---")
        for item, details in cart.items():
            cost = details['price'] * details['quantity']
            total += cost
            print(item, ":", cost)
        print("Final Total =", total)
        print("Thank you for shopping!")
        break

    elif choice == '5':
        break

    else:
        print("Invalid choice!")