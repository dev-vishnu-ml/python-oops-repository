#multiple inheritance
class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,year,cgpa):
        self.year = year
        self.cgpa = cgpa

class TA(Teacher, Student):
    def __init__(self,name,salary,year,cgpa):
        super().__init__(salary)
        Student.__init__(self,year,cgpa)
        self.name = name

ta1 = TA("vishnu",15_000,"4thyear",9.7)
print(ta1.name,ta1.salary,ta1.year,ta1.cgpa)