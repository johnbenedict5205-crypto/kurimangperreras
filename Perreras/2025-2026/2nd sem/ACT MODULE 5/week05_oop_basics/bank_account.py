class BankAccount_jbgp:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
    
    def deposit_jbgp(self, amount):
        self.balance += amount
        print("Deposit successful")
    
    def withdraw_jbgp(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_jbgp(self):
        print("Balance:", self.balance)

account_jbgp = BankAccount_jbgp("Juan", 5000)
account_jbgp.deposit_jbgp(1000)
account_jbgp.withdraw_jbgp(2000)
account_jbgp.display_balance_jbgp()

