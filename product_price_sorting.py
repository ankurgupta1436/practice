# Product Price Comparator using Insertion Sort

products = []

def add_product():
    pid = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products.append({"id": pid, "name": name, "price": price})
    print("Product added successfully!\n")

def display_products():
    if not products:
        print("No products available.\n")
        return
    for p in products:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ₹{p['price']}")
    print()

def sort_by_price():
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1
        while j >= 0 and products[j]["price"] > key["price"]:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key
    print("Products sorted by price (Low to High).\n")

while True:
    print("1. Add Product")
    print("2. Display Products")
    print("3. Sort by Price")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_product()
    elif choice == 2:
        display_products()
    elif choice == 3:
        sort_by_price()
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice!\n")
