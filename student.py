class Student():
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def get_grade(self):
        if  self.marks >= 90:
            return "A"
        elif 70 <= self.marks < 90:
            return "B"
        elif 40 <= self.marks < 70:
            return "C"
        else:
            return "F"
    
    def update_marks(self,newmarks):

        self.marks = newmarks
    
    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}, Marks : {self.marks}, Grades : {self.get_grade()}"

s1 = Student("Shahbaaz",23,91)

print(s1)
