# Example 37 - List comprehension

grades = [36, 67, 13, 89, 58, 92, 71]

passing_grades = [grade for grade in grades if grade >= 70]
print(passing_grades)