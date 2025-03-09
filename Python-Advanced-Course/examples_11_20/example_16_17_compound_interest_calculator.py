# Example 16 - Compound interest calculator

principle = float(input("Enter principle: "))
while principle <= 0:
    principle = float(input("Principle must be greater than zero. Reenter principle: "))

rate = float(input("Enter rate: "))
while rate <= 0:
    rate = float(input("Rate must be greater than zero. Reenter rate: "))

time = int(input("Enter time: "))
while time <= 0:
    time = float(input("Time must be greater than zero. Reenter time: "))

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s is ${total:.2f}")
