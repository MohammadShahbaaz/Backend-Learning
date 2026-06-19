from modules.student import add_student,search_student,show_students,delete_student,show_class_avg
from storage.json_storage import load_student

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