students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ")
        marks = float(input("Marks: "))
        students[name] = marks

    elif choice == "2":
        for name, marks in students.items():
            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            else:
                grade = "F"

            print(name, "-", marks, "-", grade)

    elif choice == "3":
        break

    else:
        print("Invalid choice")