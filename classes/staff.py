from Classes.person import Person 
# from person import Person
import csv
import os

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
    
    def all_staff():
        sets_of_staff = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")


        with open(path, newline="") as csvfile:
            staff_reader = csv.DictReader(csvfile)
            for row in staff_reader:
                new_staff = Staff(**row)
                sets_of_staff.append(new_staff)
            # print(sets_of_staff[0].employee_id)
            # # print(sets_of_staff)
            # print(sets_of_staff[0].name)
            # # print(f"{sets_of_staff} tester")
        return sets_of_staff
# print(Staff.all_staff())
# with open('../data/staff.csv', newline="") as csvfile:



# "/mnt/c/Users/kidha/Desktop/CodePlatoon/Homework_Assignments/oop-school-interface-i/data/" 
# How to hardcode file path ^^^^^^
