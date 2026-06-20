from storage.json_storage import save_student,students

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

def show_grade_A_students():
    a = [m for m in students if m["Marks"] >= 90]
    if not a:
        print("No grade A students found")
        return
    for m in a:
        print(f"{m["Name"]} - {m["Marks"]}")

def students_above(marks):
    for student in students:
        if student["Marks"] > marks:
            yield student

def show_students_above(marks):
    found = False
    for s in students_above(marks):
        found = True
        print(f"{s['Name']} - {s['Marks']}")
    if not found:
        print("No students found above that mark")

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

