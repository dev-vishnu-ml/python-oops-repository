# oop 4 pillars-> 1.Encapsulation 2.inheritance 3.polymorphism 4.abstraction
# learn and practice to make the private variables in the classes
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance #private attribute

# basically getters and setters is use to get and update the private variables

    def getattribute(self): #getters function
        return self.__balance
    
    def setattribute(self,new_name,newbalance): #setters function
        self.name = new_name
        self.__balance = newbalance

acc1 = BankAccount("rahul kumar",100_000)
print(acc1.name,acc1.getattribute())
acc1.setattribute("shardha",200_000)
print(acc1.name,acc1.getattribute())