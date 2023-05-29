from transaction_manager import withdraw, deposit, check_balance, check_transaction_history, generate_report
from user_manager import login, create_account


# Main program
def main():
    # Ask if the user wants to create an account
    create_account_option = input("Do you want to create an account? (yes/no): ")
    if create_account_option.lower() == "yes":
        create_account()

    # User authentication
    username = login()
    if not username:
        return

    # Menu
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
            withdraw(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            check_balance(username)
        elif choice == "4":
            check_transaction_history(username)
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
main()
