# main-0.py

from bank_account import BankAccount
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main-0.py <operation>")
        print("Operations: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    operation = sys.argv[1]
    account = BankAccount()

    if operation.startswith("deposit:"):
        _, amount = operation.split(":")
        account.deposit(float(amount))
        print(f"Deposited: ${amount}")
    elif operation.startswith("withdraw:"):
        _, amount = operation.split(":")
        if account.withdraw(float(amount)):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif operation == "display":
        account.display_balance()
    else:
        print("Invalid operation. Use 'deposit:<amount>', 'withdraw:<amount>', or 'display'.")

if __name__ == "__main__":
    main()

