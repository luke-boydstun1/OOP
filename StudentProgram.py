import StudentClass as SC


# s = input("Enter Student ID: ")
# n = input("Enter Name: ")
# d = input("Enter DOB: ")
# c = input("Enter Classification: ")

# student = SC.Student(s, n, d, c)
student = SC.Student(100, "Luke", "01/22/2001", "Senior")

student.registration()
student.age()

print("Student Age:", student.get_age())
print("Student Registration Dates:", student.get_registration())
