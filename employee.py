class Employee:
    def __init__(self, name, salary):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if salary < 0:
            raise ValueError("Salary can't be negative")
        
        self.name = name
        self.__salary = salary

    def get_salary(self):
        print(f"{self.name}'s salary is: {self.__salary}")

    def give_raise(self, percentage):
        self.__salary += self.__salary * percentage / 100

class Manager(Employee):
    pass

try:
    e1 = Employee(123, 20000)
except TypeError as e:
    print(f"Type error: {e}")

try:
    e2 = Employee("Shahbaaz", -5000)
except ValueError as e:
    print(f"Value error: {e}")

e3 = Employee("Shahbaaz", 20000)
e3.get_salary()
e3.give_raise(20)
e3.get_salary()