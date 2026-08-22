class student:
    def __init__(self,name,roll_number,marks):
        self.__name = name
        self.__roll_number = roll_number
        self.__marks = marks

    def set_name(self,new_name):
        if new_name == (""):
            raise(ValueError("invvalid name"))
        else:
            self.__name = new_name

    def set_roll_number(self,new_rollnumber):
        if new_rollnumber in range(1,101):
            self.__roll_number = new_rollnumber
        else:
            raise(ValueError("invalid roll number"))

    def set_marks(self,new_marks):
        if new_marks < 0:
            raise(ValueError("invalid or negative marks"))
        else:
            self.__marks = new_marks

    def get_name(self):
        print(self.__name)

    def get_rollnumber(self):
        print(self.__roll_number)

    def get_marks(self):
        print(self.__marks)

student1 = student("rahul",89,12)
student1.set_name("urvashi")
student1.set_roll_number(10)
student1.set_marks(90)
student1.get_name()
student1.get_rollnumber()
student1.get_marks()