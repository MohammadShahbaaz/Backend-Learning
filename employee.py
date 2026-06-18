class Employee:
    def __init__(self, name, salary):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if salary < 0:
            raise ValueError("Salary can't be negative")

        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary can't be negative")
        self.__salary = salary

    def give_raise(self, percentage):
        self.__salary += self.__salary * percentage / 100

    @staticmethod
    def employment_type():
        return "Full-Time Employee"

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["salary"])


class Manager(Employee):
    pass


e1 = Employee("Shahbaaz", 20000)

print(e1.salary)

e1.give_raise(20)

print(e1.salary)

print(Employee.employment_type())

employee_data = {
    "name": "Vegeta",
    "salary": 50000
}

e2 = Employee.from_dict(employee_data)

print(e2.name)
print(e2.salary)