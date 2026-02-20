# Rectangle Area Calculator

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        area = self.length * self.breadth
        print("Area:", area)
    def update_dimensions(self, l, b):
        self.length = l
        self.breadth = b
        print("Dimensions updated")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
r = Rectangle(length, breadth)
r.calculate_area()
new_length = float(input("Enter new length: "))
new_breadth = float(input("Enter new breadth: "))
r.update_dimensions(new_length, new_breadth)
r.calculate_area()