# abstraction conceptt
from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def Calculate_salary(self):
        pass

class Intern(Employee):
    def Calculate_salary(self,stipend):
        self.stipend = stipend
        return self.stipend

class FullTime_Employee(Employee):
    def Calculate_salary(self,salary):
        self.salary = salary
        return self.salary

class Contract_Employee(Employee):
    def Calculate_salary(self,working_time,money_per_hour):
        self.working_time = working_time
        self.money = money_per_hour
        return self.working_time * self.money

intern = Intern()
print(f"intern salary is: {intern.Calculate_salary(10_000)}")

fulltime = FullTime_Employee()
print(f"full time employee monthly salary is: {fulltime.Calculate_salary(90_000)}")

contract_employee = Contract_Employee()
print(f"contract employee salary = {contract_employee.Calculate_salary(12,800)}")


