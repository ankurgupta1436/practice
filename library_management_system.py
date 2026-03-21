# Simple Library Management System

books = []

def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author: ")
    books.append({"id": book_id, "name": name, "author": author, "issued": False})
    print("Book added successfully!\n")

def view_books():
    if not books:
        print("No books available.\n")
        return
    for b in books:
        print(b)
    print()

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for b in books:
        if b["id"] == book_id:
            if not b["issued"]:
                b["issued"] = True
                print("Book issued.\n")
            else:
                print("Already issued.\n")
            return
    print("Book not found.\n")

def return_book():
    book_id = input("Enter Book ID to return: ")
    for b in books:
        if b["id"] == book_id:
            b["issued"] = False
            print("Book returned.\n")
            return
    print("Book not found.\n")

while True:
    print("1.Add 2.View 3.Issue 4.Return 5.Exit")
    ch = input("Choice: ")

    if ch == "1": add_book()
    elif ch == "2": view_books()
    elif ch == "3": issue_book()
    elif ch == "4": return_book()
    elif ch == "5": break
    else: print("Invalid choice\n")