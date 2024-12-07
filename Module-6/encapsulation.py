class BankAccount:

    __balance=0

    #deposit
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    #withdraw
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawn")
        else:
            print("Insufficient balance")
    
    #check balance
    def check_balance(self):
        return self.__balance
    

obj=BankAccount()

obj.deposit(100)
print(obj.check_balance())
obj.withdraw(50)
print(obj.check_balance())
obj.withdraw(200)
print(obj.check_balance())
    
    
