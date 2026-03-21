# Simple Inventory Management System

items = []

def add_item():
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    qty = int(input("Enter Quantity: "))
    items.append({"id": item_id, "name": name, "qty": qty})
    print("Item added.\n")

def view_items():
    if not items:
        print("No items.\n")
        return
    for i in items:
        print(i)
    print()

def update_item():
    item_id = input("Enter Item ID: ")
    for i in items:
        if i["id"] == item_id:
            i["qty"] = int(input("Enter new quantity: "))
            print("Updated.\n")
            return
    print("Item not found.\n")

def delete_item():
    item_id = input("Enter Item ID: ")
    for i in items:
        if i["id"] == item_id:
            items.remove(i)
            print("Deleted.\n")
            return
    print("Item not found.\n")

while True:
    print("1.Add 2.View 3.Update 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1": add_item()
    elif ch == "2": view_items()
    elif ch == "3": update_item()
    elif ch == "4": delete_item()
    elif ch == "5": break
    else: print("Invalid choice\n")