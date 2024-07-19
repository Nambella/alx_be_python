# main-0.py

from bank_account import BankAccount
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python main-0.py <initial_balance> <deposit_amount> <withdraw_amount>")
        sys.exit(1)

    initial_balance, deposit_amount, withdraw_amount = map(float, sys.argv[1:])
    account = BankAccount(initial_balance)
    account.deposit(deposit_amount)
    if account.withdraw(withdraw_amount):
        print("Withdrawal successful.")
    else:
        print("Insufficient balance for withdrawal.")
    account.display_balance()

if __name__ == "__main__":
    main()
