# Create account
def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    balance = float(input("Enter your initial balance: "))

    # Save account details to the database
    with open("database.txt", "a") as file:
        file.write(f"{username},{password},{balance}\n")

    print("Account created successfully!")


# User authentication and login
def login():
    print("\n====Login====")
    username = input("Username: ")
    password = input("Password: ")

    # Check if account exists in the database
    with open("database.txt", "r") as file:
        for line in file:
            account = line.strip().split(",")
            if account[0] == username and account[1] == password:
                print("Login successful!")
                return username

    print("Invalid username or password.")
    return None
