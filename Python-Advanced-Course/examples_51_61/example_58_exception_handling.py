# Example 58 - Exception handling

try:
    number = float(input("Enter number: "))
    print(10.0 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Invalid number")
except Exception:
    print("Something went wrong")
finally:
    print("Doing some cleanup here")