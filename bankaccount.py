class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount>self.balance:
            return f"Insufficient Balance, Current Balance is : {self.balance}"
        else:
            self.balance -= amount
    
    def get_balance(self):
        return f"Current Balance is : {self.balance}"
    
    

owner1 = BankAccount("Shahbaaz",100000)

owner1.deposit(4000)
owner1.withdraw(10000)
print(owner1.get_balance())

print(owner1.withdraw(300000))