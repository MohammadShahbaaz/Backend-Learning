class InsufficientFundsError(Exception):
    pass

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        try:
            if amount>self.balance:
                raise InsufficientFundsError(
                    f"Insufficient Balance. Current balance is:{self.balance}"
                )
        
            self.balance -= amount

        except InsufficientFundsError:
            raise
        finally:
            print(f"Withdrawal attempt logged for {self.owner}.")
    
    
    def get_balance(self):
        return f"Current Balance is : {self.balance}"

class SavingAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate/100
        

    
owner1 = BankAccount("Shahbaaz", 100000)

owner1.withdraw(20000)
print(owner1.get_balance())