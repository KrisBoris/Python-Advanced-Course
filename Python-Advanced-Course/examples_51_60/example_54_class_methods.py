# Example 54 - Class methods

class Student:

    student_count = 0
    student_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.student_count += 1
        Student.student_gpa += gpa

    def get_info(self):
        print(f"Student {self.name} has gpa {self.gpa:.2f}")

    @classmethod
    def get_count(cls):
        return cls.student_count

    @classmethod
    def get_average_gpa(cls):
        return cls.student_gpa / cls.student_count


student1 = Student("Light", 3.9)
student2 = Student("L", 4.0)
student3 = Student("Misa", 2.5)

student1.get_info()
student2.get_info()
student3.get_info()
print(f"There are {Student.get_count()} students")
print(f"Average gpa is {Student.get_average_gpa():.2f}")
