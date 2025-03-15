# Example 47 - Class variables

class Student:

    year = 2024
    students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.students += 1


student1 = Student("Izuku", 15)
student2 = Student("Bakugo", 15)
student3 = Student("Shoto", 15)
print(f"Student: {student1.name}, age: {student1.age}")
print(f"Student: {student2.name}, age: {student2.age}")
print(f"Number of students in year {Student.year}: {Student.students}")