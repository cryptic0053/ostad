class Bank:

    def __init__(self,holder_name,initial_deposit_balance):
        self.holder_name=holder_name
        self.balance=initial_deposit_balance

    def deposit(self,amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Not enough balance")


ostad = Bank('Argha',5000)
ostad.deposit(1000)
ostad.withdraw(5000)
print(ostad.get_balance())

print(ostad.holder_name)
print(ostad.balance)
        