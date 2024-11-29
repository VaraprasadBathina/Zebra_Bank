from savings_account import SavingsAccount
from current_account import CurrentAccount
from utils import display_menu

accounts = {}

def create_account(account_type):
    name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial deposit: "))
    
    if account_type == "savings":
        account = SavingsAccount(name, initial_balance)
    elif account_type == "current":
        account = CurrentAccount(name, initial_balance)
    else:
        raise ValueError("Invalid account type.")
    
    accounts[account._generate_account_number()] = account

def perform_transaction(account_number, transaction_type):
    account = accounts.get(account_number)
    if not account:
        print("Account not found.")
        return

    amount = float(input("Enter the amount: "))
    if transaction_type == "deposit":
        account.deposit(amount)
    elif transaction_type == "withdraw":
        try:
            account.withdraw(amount)
        except ValueError as e:
            print(e)
    else:
        print("Invalid transaction type.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_account("savings")
        elif choice == "2":
            create_account("current")
        elif choice == "3":
            account_number = int(input("Enter account number: "))
            perform_transaction(account_number, "deposit")
        elif choice == "4":
            account_number = int(input("Enter account number: "))
            perform_transaction(account_number, "withdraw")
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
