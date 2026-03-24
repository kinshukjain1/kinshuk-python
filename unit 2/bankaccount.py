class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number   
        self.balance = balance                 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


# Example usage
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()

