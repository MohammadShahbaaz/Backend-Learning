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
    

class SavingAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate/100
        self.balance += interest

    
    

owner1 = BankAccount("Shahbaaz",100000)
owner2 = SavingAccount("Vegeta",500000,5)


print(owner2.get_balance())

owner2.add_interest()

print(owner2.get_balance())
