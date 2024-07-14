class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: {amount}")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

account = BankAccount("John Doe")
account.deposit(67.0)
account.withdraw(50)
account.display_balance()
