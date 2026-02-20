# Mobile Phone Details


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def apply_discount(self, amt):
        self.price = self.price - amt
        print("Discount applied :", amt)
    def display_mobile(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
brand = input("Enter brand : ")
model = input("Enter model : ")
price = float(input("Enter price : "))
m = Mobile(brand, model, price)
disc = float(input("Enter discount amount : "))
m.apply_discount(disc)
m.display_mobile()