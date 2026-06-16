class Employee():
    def __init__(self,salary):
        self.__salary = salary
    
    def get_salary(self):
        print(f"Your salary is : {self.__salary}")
    
    def give_raise(self,percentage):
        self.__salary += self.__salary * percentage/100
    
class Manager(Employee):
    pass


e1 = Employee(20000)
e1.give_raise(20)

e1.get_salary()