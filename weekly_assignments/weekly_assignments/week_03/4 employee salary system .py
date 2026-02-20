# Employee Salary System 

class Employee:
    def __init__(self, name, empid, sal):
        self.name = name
        self.empid = empid
        self.sal = sal
    def increase_salary(self, amt):
        self.sal = self.sal + amt
        print("Salary increased by:", amt)
    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.empid)
        print("Salary:", self.sal)
name = input("Enter employee name: ")
empid = input("Enter employee ID: ")
sal = float(input("Enter salary: "))
e = Employee(name, empid, sal)
inc = float(input("Enter increase amount: "))
e.increase_salary(inc)
e.display_details()