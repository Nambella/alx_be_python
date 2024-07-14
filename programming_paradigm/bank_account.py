class BankAccount:
    def __init__(self, account_holder_name, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount:.1f}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
