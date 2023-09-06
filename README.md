# BANKING SYSTEM PROJECT

This Python code represents a simple banking system that allows users to perform basic operations like account login, deposit, and withdrawal.

# 1.BankAccount Class:
This class is used to create and manage bank accounts.

Bank_detail method is used to initialize a bank account with the following parameters:
account_number: Account number
pin: PIN for account access
user_name: User's name
password: Password for account access
balance: Initial account balance (default is set to 0)

login method is used to check if the provided user_name and password . If they match, it returns True, indicating a successful login; otherwise, it returns False.

deposit method allows the user to deposit a specified amount into their account. It checks if the provided user_name and password ,and it credited to the balance and shows its print statement.


withdraw method allows the user to withdraw  amount from their account,here also check the provided user name and password if the condition is satisfied,
it check the withrawl amount is less than the balance,the amount will be debited and shows ,amount debited successfully.

Then we creating a variable name'account',assigning the object bank account and calling each method using this variable.

# 2.Main Program:
The program starts with a welcome message and then creates an instance of the BankAccount class.
It presents a menu of options to the user:
Option 1: Account login
Option 2: Amount deposit
Option 3: Amount withdrawal
The user is prompted to enter their choice, and their choice is stored in the select_option variable.

Depending on the selected option, the program takes further actions:
The code then checks the value of select_option and executes the corresponding block of code based on the user's choice.
Option 1: Account Login:
If the user chooses option 1, they are asked by to enter their username and password.
The login method of the account object is called to check if the provided username and password. 
If they match, it prints "Login successful"; otherwise, it prints "Invalid username or password."

Option 2: Deposit:
If the user chooses option 2, they are asked by to enter their username, password, and the amount they want to deposit. 
The deposit method of the account object is called to process the deposit

Option 3: Withdrawal:
If the user chooses option 3, they are asked by to enter their username, password, and the amount they want to withdraw.
The withdraw method of the account object is called to process the withdrawal.



