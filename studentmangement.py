class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:

    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        # Automatically add student to database
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print("Error: Student is already enrolled.")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully!")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Error: Student is not enrolled.")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully!")

    def view_student_info(self):
        print("\n----- Student Information -----")
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Department:", self.__department)
        print("Enrollment Status:",
              "Enrolled" if self.__is_enrolled else "Not Enrolled")


# Manually initialize students
student1 = Student("101", "Parvez", "CSE", True)
student2 = Student("102", "Rahim", "EEE", False)
student3 = Student("103", "Karim", "BBA", True)


# Menu-driven system
while True:

    print("\n===== Student Database Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if not StudentDatabase.student_list:
            print("No students found.")

        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "2":

        student_id = input("Enter Student ID: ")

        found = False

        for student in StudentDatabase.student_list:
            if student._Student__student_id == student_id:
                student.enroll_student()
                found = True
                break

        if not found:
            print("Error: Invalid Student ID.")

    elif choice == "3":

        student_id = input("Enter Student ID: ")

        found = False

        for student in StudentDatabase.student_list:
            if student._Student__student_id == student_id:
                student.drop_student()
                found = True
                break

        if not found:
            print("Error: Invalid Student ID.")

    elif choice == "4":
        print("Thank you for using Student Database!")
        break

    else:
        print("Invalid choice! Please try again.")