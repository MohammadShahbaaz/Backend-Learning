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

def add_student():
    name = input("Enter Student Name : ")
    
    try:
        marks = int(input("Enter marks of the Student : "))
    
    except ValueError:
        print("Marks must be a number.")
        return
    
    student = {
        "Name" : name,
        "Marks" : marks 
    }

    students.append(student)

    save_student()

    print("Student saved successfully")

def show_students():
    if not students:
        print("No Student found")
        return
    
    for student in students:
        print(f"{student["Name"]} - {student["Marks"]}")

def search_student():
    sname = input("Enter Student name you wanna search : ")
    found = False

    for student in students:
        if student["Name"].lower() == sname.lower():
            found = True
            print(f"{student['Name']} - {student['Marks']}")
            break
        
    if not found:
        print("Student not found")

def delete_student():
    dname = input("Enter Student name you wanna delete : ")
    found = False

    for student in students:
        if student["Name"].lower() == dname.lower():
            found = True
            print(f"{student['Name']} - {student['Marks']} \nRecords Deleted")
            students.remove(student)
            save_student()
            break
        
    if not found:
        print("Student not found")


def show_class_avg():
    if not students:
        print("No Student found")
        return
    
    total = 0 

    for student in students:
        total += student["Marks"]

    avg = total/len(students)

    print(f"Class Average is : {avg:.2f}")

load_student()

while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Show Class Average")
    print("4. Search Student")
    print("5. Delete Student Record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        show_class_avg()
    
    elif choice == "4":
        search_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")