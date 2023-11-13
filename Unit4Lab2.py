
#class for bankaccount
class Account:
    #define the attributes
    def __init__(self, accountNumber, customerName, balance):
        self.number = accountNumber
        self.name = customerName
        self.balance = balance
    #define methods
    def deposit(self, deposit):
        self.deposit = deposit
    def withdraw(self, withdraw):
        self.withdraw = withdraw
    def display(self, display):
        self.display = display