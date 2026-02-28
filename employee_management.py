# Employee Management using OOP Concepts

class Employee:
    
    # Constructor
    def __init__(self, emp_id, emp_name, department, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.salary = salary

    # Method to display employee details
    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.emp_name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("---------------------------")

    # Method to check high salary
    def is_high_salary(self):
        if self.salary > 50000:
            return True
        return False


# Creating objects
emp1 = Employee(101, "Aditya Awasthi", "HR", 35000)
emp2 = Employee(102, "Ankit Kumar", "IT", 50000)
emp3 = Employee(104, "Ankur Gupta", "Content Creator", 200000)

# Display details
emp1.display()
emp2.display()
emp3.display()

# Check high salary employees
print("High Salary Employees:")
for emp in [emp1, emp2, emp3]:
    if emp.is_high_salary():
        print(emp.emp_name)