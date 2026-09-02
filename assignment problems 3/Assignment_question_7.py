# constructor overloading with default perameters
class Person:
    def __init__(self,name,age = None,address = None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"name is: {self.name}", end=" ")
        if self.age is not None:
            print(f"Age is :{self.age}", end="")
        if self.address is not None:
            print(f"Address is {self.address}")
        print()

p1 = Person("vishnu")
p1.display()

p2 = Person("vishnu",18)
p2.display()

p3 = Person("vishnu",18,"rajasthan")
p3.display()

