# Example 8 - Simple calculator

operator = input("Enter operator: ")
value_1 = float(input("Enter first number: "))
value_2 = float(input("Enter second number: "))
result = None

if operator == "+":
    result = value_1 + value_2
elif operator == "-":
    result = value_1 - value_2
elif operator == "*":
    result = value_1 * value_2
elif (operator == "/" or operator == ":") and value_2 != 0:
    result = value_1 / value_2

if result is not None:
    result = round(result, 2)
    print(f"Result: {result}")
else:
    print("Incorrect operator or value")
