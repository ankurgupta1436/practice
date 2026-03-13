class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("-" * 30)


class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp):
        if emp.emp_id in self.employees:
            print("Employee already exists.")
        else:
            self.employees[emp.emp_id] = emp
            print("Employee added successfully.")

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee removed.")
        else:
            print("Employee not found.")

    def search_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].display()
        else:
            print("Employee not found.")

    def display_all(self):
        if not self.employees:
            print("No employees available.")
        else:
            for emp in self.employees.values():
                emp.display()


def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Search Employee")
        print("4. Display All Employees")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            emp = Employee(emp_id, name, dept, salary)
            manager.add_employee(emp)

        elif choice == "2":
            emp_id = input("Enter Employee ID to remove: ")
            manager.remove_employee(emp_id)

        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            manager.search_employee(emp_id)

        elif choice == "4":
            manager.display_all()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option")


main()