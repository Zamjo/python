class Account:
    def __init__(self):
        self.balance = 0
    def create(self):
        self.acno = int(input("Enter Account number : "))
        self.name = str(input("Enter Name : "))
        print("Account number : ", self.acno)
        print("Name : ", self.name)
        print("Account created")
    def deposit(self):
        amount = int(input("Enter the amount to Diposit : "))
        self.balance += amount
        print("Balance : ",self.balance)
    def withdraw(self):
        amount = int(input("Enter the amount to Withdraw : "))
        if (amount > self.balance):
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("your remaining balance : ", self.balance)

account = Account()
account.create()
account.deposit()
account.withdraw()