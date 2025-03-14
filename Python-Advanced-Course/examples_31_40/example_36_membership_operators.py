# Example 36 - Membership operators

grades = {"Walter": 5, "Jesse": 3, "Mike": 4, "Hank": 4.5}

student = input("Enter student's name: ")

if student in grades:
    print(f"{student} got {grades.get(student)}")
else:
    print(f"{student} was not found")