class BankAccount:
    account_balance = 0
    def __init__(self, account_balance):
        self.account_balance = account_balance
    def deposit(self,amount):
        self.account_balance +=amount
        return f"Deposited: ${amount}"
    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return f"Withdrew: ${amount}"
        else:
            return "Insufficient funds."
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}.00")
    