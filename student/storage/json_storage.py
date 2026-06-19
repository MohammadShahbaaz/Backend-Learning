import json


students = []

def load_student():
    global students

    try:
        with open("student.json","r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    

def save_student():
    with open("student.json","w") as file:
        json.dump(students, file, indent = 4)