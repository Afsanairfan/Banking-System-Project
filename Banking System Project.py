class BankAccount:
    def Bank_detail(self, account_number, pin, user_name, password, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.user_name = user_name
        self.password = password

    def login(self, user_name, password):
        if user_name == self.user_name and password == self.password:
            return True
        else:
            return False

    def deposit(self, deposit_amount, user_name, password):
        if user_name == self.user_name and password == self.password:
            self.balance += deposit_amount
            print("Amount deposited successfully.")
            print("Current balance:", self.balance)
        else:
            print("Invalid username or password.")

    def withdraw(self, withdrawal_amount, user_name, password):
        if user_name == self.user_name and password == self.password:
            if withdrawal_amount <= self.balance:
                self.balance -= withdrawal_amount
                print("Amount withdrawn successfully.")
                print("Current balance:", self.balance)
            else:
                print("Insufficient bank balance.")
        else:
            print("Invalid username or password.")


print("Welcome to the Banking System")

# Creating a bank account
account = BankAccount()
account.Bank_detail('123456789', '1234', 'Afsana', '12345', 1000)

# Displaying menu options
print("1. Account login")
print("2. Amount deposit")
print("3. Amount withdrawal")

# Selecting an option
select_option = int(input("Enter the option: "))

if select_option == 1:
    # Account login
    user_name = input("Enter the user name: ")
    password = input("Enter the password: ")
    if account.login(user_name, password):
        print("Login successful.")
    else:
        print("Invalid username or password.")

elif select_option == 2:
    # Deposit
    user_name = input("Enter the user name: ")
    password = input("Enter the password: ")
    amount = float(input("Enter the amount to deposit: "))
    account.deposit(amount, user_name, password)

elif select_option == 3:
    # Withdrawal
    user_name = input("Enter the user name: ")
    password = input("Enter the password: ")
    amount = float(input("Enter the amount to withdraw: "))
    account.withdraw(amount, user_name, password)

else:
    print("Invalid option.")


