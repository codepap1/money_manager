import datetime


class TransactionManager:
    def __init__(self):
        self.filename = "database.txt"

    def get_account_info(self, username):
        with open(self.filename, "r") as file:
            for line in file:
                account = line.strip().split(",")
                if account[0] == username:
                    return account
        return None

    def update_account(self, updated_account):
        updated_lines = []
        with open(self.filename, "r") as file:
            for line in file:
                account = line.strip().split(",")
                if account[0] == updated_account[0]:
                    updated_lines.append(",".join(updated_account))
                else:
                    updated_lines.append(line)

        with open(self.filename, "w") as file:
            file.writelines(updated_lines)

    def deposit(self, username):
        while True:
            try:
                amount = float(input("Enter the amount to deposit: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if amount <= 0:
                print("Invalid amount. Amount must be greater than 0.")
                continue

            account = self.get_account_info(username)
            if account:
                account[2] = str(float(account[2]) + amount)
                account.append(f"{datetime.datetime.now()},Deposit,{amount}")
                self.update_account(account)
                print(f"Deposited ${amount}. New balance: ${account[2]}")
                break

    def withdraw(self, username):
        while True:
            try:
                amount = float(input("Enter the amount to withdraw: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if amount <= 0:
                print("Invalid amount. Amount must be greater than 0.")
                continue

            account = self.get_account_info(username)
            if account:
                if float(account[2]) >= amount:
                    account[2] = str(float(account[2]) - amount)
                    account.append(f"{datetime.datetime.now()},Withdraw,{amount}")
                    self.update_account(account)
                    print(f"Withdrew ${amount}. New balance: ${account[2]}")
                    break
                else:
                    print("Insufficient balance.")

    def check_balance(self, username):
        account = self.get_account_info(username)
        if account:
            balance = float(account[2])
            print(f"Your current balance is: ${balance}")

    def check_transaction_history(self, username):
        account = self.get_account_info(username)
        if account:
            transactions = account[3:]
            if len(transactions) == 0:
                print("No transactions found.")
            else:
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)

    def generate_report(self):
        print("Overall Report:")
        with open(self.filename, "r") as file:
            for line in file:
                account = line.strip().split(",")
                username = account[0]
                balance = float(account[2])
                print(f"Username: {username}, Balance: ${balance}")
