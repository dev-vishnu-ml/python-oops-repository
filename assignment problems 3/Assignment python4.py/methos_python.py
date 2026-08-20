# practice and learn the methods in pyhton -> 1.instance 2.static 3.classmethod
class student:
    college_name = "abc colllege"
    def __init__(self,student_name,cgpa):
        self.student_name = student_name
        self.cgpa = cgpa

    @classmethod
    def get_clgname(cls):
        print(f"college name is : {cls.college_name}")

    @staticmethod
    def calculate_discount(fees,discount):
        final_fees = fees-(discount*fees/100)
        print(f"your final fees {final_fees}")

    def get_student_info(self):
        print(f"student name is: {self.student_name} and cgpa is {self.cgpa} college is: {self.college_name}")

student1 = student("vishnu",9.1)
student1.get_clgname()
student1.calculate_discount(45_300,10)
student1.get_student_info()

