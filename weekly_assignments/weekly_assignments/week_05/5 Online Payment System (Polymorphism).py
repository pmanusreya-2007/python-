#5 . Online Payment System (Polymorphism)
# Base class
class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)


# Subclass CreditCardPayment
class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Payment of", amount, "processed using Credit Card")


# Subclass UPIPayment
class UPIPayment(Payment):
    def pay(self, amount):
        print("Payment of", amount, "processed using UPI")


# Subclass WalletPayment
class WalletPayment(Payment):
    def pay(self, amount):
        print("Payment of", amount, "processed using Wallet")


# Create objects
payment1 = CreditCardPayment()
payment2 = UPIPayment()
payment3 = WalletPayment()

# Process payments (Polymorphism)
payments = [payment1, payment2, payment3]

for payment in payments:
    payment.pay(1000)