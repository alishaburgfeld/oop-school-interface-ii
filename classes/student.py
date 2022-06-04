from Classes.person import Person 
# from person import Person 
import csv
import os

class Student(Person):
    def __init__(self, name, age, role, password, school_id):
        super().__init__(name, age, role, password)
        self.school_id = school_id
    def __str__(self):
        return f"{self.name}\n---------------\nage: {self.age}\nid: {self.role}"


    def all_students():
        sets_of_students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path, newline="") as csvfile:
            student_reader = csv.DictReader(csvfile)
            for row in student_reader:
                new_student = Student(**row)
                sets_of_students.append(new_student)
            # # print(sets_of_students)
            # print(sets_of_students[0].name)
            # # print(f"{sets_of_students} tester")
        return sets_of_students
       
        

# print(Student.all_students())
# with open('../data/students.csv', newline="") as csvfile:
