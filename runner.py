from Classes.school import School
# from Classes.staff import Staff
# from Classes.student import Student

school = School('Ridgemont High') 

# print(school.staff[0].role)


counter=0
while counter<6:
    mode=input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    if mode == "1":
        school.list_students()
        #is this the most efficient way to do this? just keep putting mode at the end of each option? seems redundant
    elif mode == "2":
        student_id = input("Enter student id:")
        student = school.find_student_by_id(student_id)
        print(str(student))
    elif mode =="5":
        print("Ta ta for now!")
        counter=6

        #mode=input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")