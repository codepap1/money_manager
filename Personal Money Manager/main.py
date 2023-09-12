from user_manager import UserManager
from transaction_manager import TransactionManager


def main():
    user_manager = UserManager()
    transaction_manager = TransactionManager()

    create_account_option = input("Do you want to create an account? (yes/no): ")
    if create_account_option.lower() == "yes":
        user_manager.create_account()

    username = user_manager.login()
    if not username:
        return

    while True:
        print("\n===== Personal Money Manager =====")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Generate Overall Report")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            transaction_manager.withdraw(username)
        elif choice == "2":
            transaction_manager.deposit(username)
        elif choice == "3":
            transaction_manager.check_balance(username)
        elif choice == "4":
            transaction_manager.check_transaction_history(username)
        elif choice == "5":
            transaction_manager.generate_report()
        elif choice == "6":
            print("\n====================================")
            print("Logged out.")
            break
        else:
            print("\n====================================")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
