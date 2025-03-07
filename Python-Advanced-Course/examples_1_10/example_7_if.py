# Example 7 - If statements

age = input("Enter your age")

# order of if statements matters; statements are checked sequentially from up to bottom
if age >= 100:
    print("You are too old to sing up")
elif age >= 18:
    print("You are an adult")
else:
    print("You are too young to sign")
