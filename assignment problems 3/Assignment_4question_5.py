# inheritance concept
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats = seats
    def get_carinfo(self):
        print(f"car brand is: {self.brand}, model is :{self.model} and seats is = {self.seats}seater")

class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc

    def get_bike_info(self):
        print(f"bike brand is : {self.brand} and model is {self.model} and enginee_cc is {self.engine_cc}")

bike = Bike("ktm","2020","150_cc")
bike.get_bike_info()

car = Car("Tata","Harier",8)
car.get_carinfo()