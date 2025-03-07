# Example 9 - Weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter unit (K for kg or P for pounds): ")
unit_name = None

if unit == "K":
    weight *= 2.205
    unit_name = "lbs"
elif unit == "P":
    weight /= 2.205
    unit_name = "kgs"

if unit_name is not None:
    weight = round(weight, 1)
    print(f"Your weight is {weight} {unit_name}")
else:
    print("Incorrect unit")