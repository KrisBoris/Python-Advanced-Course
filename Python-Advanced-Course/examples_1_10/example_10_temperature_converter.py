# Example 10 - Temperature converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temperature = float(input("Enter temperature: "))
unit_name = None

if unit == "C":
    temperature = round(temperature * 9.0 / 5.0 + 32, 1)
    unit_name = "F"
elif unit == "F":
    temperature = round((temperature - 32) * 5.0 / 9.0, 1)
    unit_name = "C"

if unit_name is not None:
    print(f"Temperature equals: {temperature} {unit_name}")
else:
    print("Incorrect unit")
