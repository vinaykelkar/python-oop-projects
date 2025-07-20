class Account:
    def __init__(self,account_number,holder_name,balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError(f"Deposit amount should be positive")
        self.balance = self.balance + amount
        print(f"Deposited amount INR {amount}. New Balance is INR {self.balance}")
    
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError(f"Withdrawal amount should be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient Funds")
        self.balance = self.balance - amount
        print(f"Withdrawal amount is INR {amount} and new balance is now INR {self.balance}")

    def display_balance(self):
        print(f"Balance for account number {self.account_number}, Holder name : {self.holder_name}, is INR{self.balance}")    

class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, withdrawal_limit=10000):
        super().__init__(account_number, holder_name, balance)
        self.withdrawal_limit = withdrawal_limit
    
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            raise ValueError(f"Cannot withdraw more than INR {self.withdrawal_limit} in one transaction")
        super().withdraw(amount)

class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError(f"Withdrawal limit exceeded")
        self.balance = self.balance - amount
        print(f"Withdrew amount INR {amount} and new balance is INR {self.balance}")
