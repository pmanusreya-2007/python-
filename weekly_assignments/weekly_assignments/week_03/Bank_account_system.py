class BankAccount:
    def __init__(self, name, acc, bal):
        self.name = name
        self.acc = acc
        self.bal = bal
    def deposit(self, amt):
        self.bal = self.bal + amt
        print("Amount deposited:", amt)
    def withdraw(self, amt):
        if amt > self.bal:
            print("Not enough balance")
        else:
            self.bal = self.bal - amt
            print("Amount withdrawn:", amt)
    def display_balance(self):
        print("Name:", self.name)
        print("Account Number:", self.acc)
        print("Balance:", self.bal)
name = input("Enter name: ")
acc = input("Enter account number: ")
bal = float(input("Enter balance: "))
a = BankAccount(name, acc, bal)
dep = float(input("Enter deposit amount: "))
a.deposit(dep)
wd = float(input("Enter withdrawal amount: "))
a.withdraw(wd)
a.display_balance()
