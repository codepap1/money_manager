import datetime


# Withdraw money
def withdraw(username):
    amount = float(input("Enter the amount to withdraw: "))

    # Update account balance in the database
    updated_lines = []
    with open("database.txt", "r") as file:
        for line in file:
            account = line.strip().split(",")
            if account[0] == username:
                if amount > 0 and amount <= float(account[2]):
                    account[2] = str(float(account[2]) - amount)
                    account.append(f"{datetime.datetime.now()},Withdraw,{amount}")
                else:
                    print("Invalid amount or insufficient balance.")
            updated_lines.append(",".join(account) + "\n")

    # Rewrite the database with updated account details
    with open("database.txt", "w") as file:
        file.writelines(updated_lines)


# Deposit money
def deposit(username):
    amount = float(input("Enter the amount to deposit: "))

    # Update account balance in the database
    updated_lines = []
    with open("database.txt", "r") as file:
        for line in file:
            account = line.strip().split(",")
            if account[0] == username:
                if amount > 0:
                    account[2] = str(float(account[2]) + amount)
                    account.append(f"{datetime.datetime.now()},Deposit,{amount}")
                else:
                    print("Invalid amount.")
            updated_lines.append(",".join(account) + "\n")

    # Rewrite the database with updated account details
    with open("database.txt", "w") as file:
        file.writelines(updated_lines)


# Check balance
def check_balance(username):
    with open("database.txt", "r") as file:
        for line in file:
            account = line.strip().split(",")
            if account[0] == username:
                balance = float(account[2])
                print(f"Your current balance is: ${balance}")
                break


# Check transaction history
def check_transaction_history(username):
    with open("database.txt", "r") as file:
        for line in file:
            account = line.strip().split(",")
            if account[0] == username:
                transactions = account[3:]
                if len(transactions) == 0:
                    print("No transactions found.")
                else:
                    print("Transaction History:")
                    for transaction in transactions:
                        print(transaction)
                break


# Generate overall report
def generate_report():
    print("Overall Report:")
    with open("database.txt", "r") as file:
        for line in file:
            account = line.strip().split(",")
            username = account[0]
            balance = float(account[2])
            print(f"Username: {username}, Balance: ${balance}")
