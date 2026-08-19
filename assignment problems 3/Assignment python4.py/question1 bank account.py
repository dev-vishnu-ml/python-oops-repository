# create a bankaccount class with attributes account_number,owner_name,balance
# add methods to deposit withdraw and check_balance 
class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,NewAmmount):
        self.balance += NewAmmount
        return self.balance

    def withdraw_amount(self,withdrawMoney):
        if withdrawMoney > self.balance:
            print("insufficient balance")

        else:
           self.balance -= withdrawMoney
           print("money withdraw sucess fully:")

    def check_balance(self):
        print(f"your balance is: {self.balance}")

acc1 = BankAccount(8489898,"shivpal",10000)
acc1.check_balance()

acc1.deposit(5000)

acc1.check_balance()

acc1.withdraw_amount(111000)

acc1.check_balance()