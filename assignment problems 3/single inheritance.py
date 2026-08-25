# single inheritance
class Employee:
    start_time = "9am"
    End_time = "4pm"
    def change_start_time(self,new_time):
        self.start_time = new_time

class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject

t1 = Teacher("python")
t1.change_start_time("10am")
print(t1.start_time, t1.End_time, t1.subject)

