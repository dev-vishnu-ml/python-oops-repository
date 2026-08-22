class Employee:  #parent/base class
    starting_time = "10am"
    end_time = "5pm"
    def change_end_time(self,new_time):  #methods it is accessible inside derived class
        self.end_time = new_time

class Teacher(Employee):  #derived class
    def __init__(self,subject):
        self.subject = subject

class Adminstaff(Employee): #2nd derived class
    def __init__(self,role):
        self.role = role

Teacher1 = Teacher("Maths")
print(Teacher1.subject,Teacher1.starting_time,Teacher1.end_time)
staff1 = Adminstaff("Manager")
staff1.change_end_time("6pm")
print(staff1.role,staff1.starting_time,staff1.end_time)

