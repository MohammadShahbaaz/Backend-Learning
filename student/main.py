from modules.student import add_student,search_student,show_students,delete_student,show_class_avg,show_grade_A_students,show_students_above
from storage.json_storage import load_student

load_student()

while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Show Class Average")
    print("4. Students with grade A")
    print("5. Search Student")
    print("6. Delete Student Record")
    print("7. Student Above given marks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        show_class_avg()

    elif choice == "4":
        show_grade_A_students()
    
    elif choice == "5":
        search_student()

    elif choice == "6":
        delete_student()
    
    elif choice == "7":
        try:
            marks = int(input("Show students above what marks? "))
            show_students_above(marks)
        except ValueError:
            print("Enter a valid number.")

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")