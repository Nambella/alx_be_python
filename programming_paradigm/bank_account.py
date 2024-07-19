class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    account = BankAccount()  # Create an account with initial balance 0
    account.deposit(100)    # Deposit $100
    account.withdraw(50)    # Withdraw $50
    account.display_balance()  # Display the remaining balance
