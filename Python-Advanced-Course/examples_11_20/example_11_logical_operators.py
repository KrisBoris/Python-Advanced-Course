# Example 11 - Logical operators

temp = 25
is_raining = False

if temp > 36 or is_raining:
    print("Do not go outside")
elif temp < 36 and not is_raining:
    print("You can go outside")