# from Classes.student import Student
# from Classes.staff import Staff
from Classes.student import Student
from Classes.staff import Staff


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def list_students(self):
        all_students= Student.all_students()
        for i, student in enumerate(all_students):
            print(f"{i+1}. {student.name} {student.school_id}")

    def find_student_by_id(self,id):
        all_students= Student.all_students()
        for student in all_students:
            if student.school_id==id:
                return student