class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self,amount):
        if amount >= 0:
            self.account_balance += amount
        # return f"Deposited: ${amount}"
    
    def withdraw(self,amount):
        if amount >= 0:
            if self.account_balance < amount:
                return True
            else:
                self.account_balance -= amount
                return False
        return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    