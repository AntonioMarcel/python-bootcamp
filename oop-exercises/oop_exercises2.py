class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance + money
        print("Deposit accepted")

    def withdraw(self, money):
        if self.balance - money >= 0: 
            self.balance = self.balance - money
            print("Withdrawal accepted")
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
acc1 = BankAccount('Xarope', 100)
print(acc1)

print(acc1.balance)
acc1.withdraw(100)
acc1.deposit(500)
acc1.withdraw(1000)
print(acc1.balance)