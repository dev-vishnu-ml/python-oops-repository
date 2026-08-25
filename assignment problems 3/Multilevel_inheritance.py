# Multilevel Inheritance
class Employee:
    start_time = "10am"
    end_time = "5pm"

class Adminstaff(Employee):
    def __init__(self,role):
        self.role = role

class  Account(Adminstaff):
    def __init__(self,name,salary,role):
        super().__init__(role)
        self.name = name
        self.salary = salary
    

acc1 = Account("vishnu",15_000,"CA")
print(acc1.name,acc1.salary,acc1.role,acc1.start_time,acc1.end_time)
