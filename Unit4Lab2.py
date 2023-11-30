

class bankAccount:
    """Constructor"""
    def __init__(self, accountNumber, customerName, balance):
        self.accountNumber = accountNumber
        self.customerName = customerName
        self.balance = balance
    
    """Methods"""
    def deposit(self, value):
        self.balance += value
        return f"New Balance ${self.balance}"
    
    def withdraw(self, value):
        self.balance -= value
        return f"New Balance ${self.balance}"
    
    def display(self):
        return f"Account Number: {self.accountNumber}  Name: {self.customerName}  Balance: ${self.balance}"
    

number = int(input("Enter your acount number: "))
name = input("Enter your name: ")
balance = float(input("Enter your balance: "))

account = bankAccount(number, name, balance)

choice = int(input("Would you like to: \n 1. Deposit \n 2. Widthdraw \n 3. Display \n >"))

if choice == 1:
    value = int(input("How much would you like to deposit: "))
    print(account.deposit(value))
elif choice == 2:
    value = int(input("How much would you like to withdraw: "))
    print(account.withdraw(value))
elif choice ==3:
    print(account.display())
else:
    print("Invalid Input")






