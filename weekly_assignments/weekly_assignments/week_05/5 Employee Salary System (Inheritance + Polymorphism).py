#5 . Employee Salary System (Inheritance + Polymorphism)
# Base class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# Subclass Manager
class Manager(Employee):
    def calculate_salary(self):
        bonus = 5000
        return self.base_salary + bonus


# Subclass Developer
class Developer(Employee):
    def calculate_salary(self):
        bonus = 3000
        return self.base_salary + bonus


# Subclass Intern
class Intern(Employee):
    def calculate_salary(self):
        deduction = 1000
        return self.base_salary - deduction


# Create objects
emp1 = Manager("Arun", 40000)
emp2 = Developer("Neha", 35000)
emp3 = Intern("Rahul", 15000)

# Display salary details (Polymorphism)
employees = [emp1, emp2, emp3]

for emp in employees:
    print("Name:", emp.name)
    print("Salary:", emp.calculate_salary())
    print()