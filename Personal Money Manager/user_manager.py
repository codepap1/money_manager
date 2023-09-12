class UserManager:
    def __init__(self):
        self.filename = "database.txt"

    def create_account(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        balance = float(input("Enter your initial balance: "))

        with open(self.filename, "a") as file:
            file.write(f"{username},{password},{balance}\n")

        print("\n====================================")
        print("Account created successfully!")

    def login(self):
        while True:
            print("\n======== Login ========")
            username = input("Username: ")
            password = input("Password: ")

            # Check if account exists in the database
            with open(self.filename, "r") as file:
                for line in file:
                    account = line.strip().split(",")
                    if account[0] == username and account[1] == password:
                        print("\n====================================")
                        print("Login successful!")
                        return username

            print("\n====================================")
            print("Invalid username or password. Please try again.")
