import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <initial_balance> <operation> <amount>")
        return

    initial_balance = float(sys.argv[1])
    operation = sys.argv[2]
    amount = float(sys.argv[3]) if len(sys.argv) > 3 else 0

    account = BankAccount(initial_balance)

    if operation == "deposit":
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}")
    elif operation == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds")
    elif operation == "balance":
        account.display_balance()
    else:
        print("Invalid operation. Use 'deposit', 'withdraw', or 'balance'.")

    account.display_balance()

if __name__ == "__main__":
    main()
