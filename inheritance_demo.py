class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def show_details(self):
        self.show()
        print("Salary:", self.salary)


emp = Employee("Ankit", 50000)
emp.show_details()