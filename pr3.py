students = []

student_data = {}

print("Welcome to Student Data Organizer!")

while True:

    print("\n---Student Data Organizer---")

    print("1. Add Student")

    print("2. Display All Students")

    print("3. Update Student Information")

    print("4. Delete Student")

    print("5. Display Subjects Offered")

    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n--- Add Student ---")

        student_id = int(input("Enter Student ID: "))

        if student_id in student_data:

            print("Student ID already exists!")

        else:

            name = input("Name:")

            age = int(input("Age:"))

            grade = input("Grade:")

            dob = input("Date of Birth (YYYY-MM-DD):")

            subject_input = input("Enter Subjects (comma-separated):")

            subjects = set()

            for subject in subject_input.split(","):

                subjects.add(subject.strip())
                info = (student_id, dob)

            student={"info": info,"name": name,"age": age,"grade": grade,"subjects": subjects}

            students.append(student)

            student_data[student_id] = student

            print("Student added successfully!")

    elif choice == "2":

        print("\n--- All Students ---")

        if not students:

            print("No students found!")

        else:

            for student in students:

                student_id, dob = student["info"]

                subjects = ", ".join(sorted(student["subjects"]))

                print(f"ID: {student_id} | "f"Name: {student['name']} | "f"Age: {student['age']} | "f"Grade: {student['grade']} | "f"DOB: {dob} | "f"Subjects: {subjects}")

    elif choice == "3":

        print("\n--- Update Student ---")

        student_id = int(input("Enter Student ID: "))

        if student_id not in student_data:

            print("Student not found!")

        else:

            student = student_data[student_id]

            print("1. Update Name")

            print("2. Update Age")

            print("3. Update Grade")

            print("4. Update Subjects")

            update_choice = input("Enter your choices: ").split(",")

            if "1" in update_choice:
                student["name"] = input("Enter new name: ")
            if "2" in  update_choice:
                student["age"] = int(input("Enter new age: "))
            if "3" in update_choice:
                student["grade"] = input("Enter new grade: ")
            if "4" in update_choice:
                subject_input = input("Enter new subjects (comma-separated): ")

                new_subjects = set()

                for subject in subject_input.split(","):

                    new_subjects.add(subject.strip())

                student["subjects"] = new_subjects
            
                print("Student updated successfully!")

            else:

                print("Invalid choice!")
    elif choice == "4":

        print("\n--- Delete Student ---")

        student_id = int(input("Enter Student ID: "))

        if student_id not in student_data:

            print("Student not found!")

        else:

            for student in students:

                if student["info"][0] == student_id:

                    students.remove(student)

                    break

            del student_data[student_id]

            print(f"Student ID {student_id} deleted successfully!")

    elif choice == "5": 

        print("\n--- Subjects Offered ---")

        all_subjects = set()

        for student in students:

            all_subjects.update(student["subjects"])

        if not all_subjects:

            print("No subjects found!")

        else:

            print("Unique Subjects Offered:")

            for subject in sorted(all_subjects):

                print("-", subject)

    elif choice == "6":

        print("\nthank you for using student data oraganizer!")
        print("exiting the program.Goodbye!")

        break

    else:

        print("Invalid choice! Please enter a number from 1 to 6.")
