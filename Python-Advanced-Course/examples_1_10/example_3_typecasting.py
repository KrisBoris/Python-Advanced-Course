# Example 3 - Typecasting

name = "Andrew"
number = "1"
age = 20
gpa = 3.8
is_rushing = True

print(type(name))

# truncated the decimals
gpa = int(gpa)
print(gpa)

# adds decimal point
age = float(age)
print(age)

# converting String to int throws error
#name = int(name)
#print(name)

# converts to either 0 or 1
is_rushing_int = int(is_rushing)
print(is_rushing_int)

# converts to either 0.0 or 1.0
is_rushing_float = float(is_rushing)
print(is_rushing_float)

# returns "True" or "False"
is_rushing_str = str(is_rushing)
print(is_rushing_str + "?")

# True if String is not empty, else False
name = bool(name)
print(name)

# True if > 0, else False
age = bool(age)
print(age)

numero = int(number)
print(numero)