# Example 17 - For loops

for i in range(0, 10):
    print(i + 1)

for i in reversed(range(0, 10)):
    print(i + 1)

# Third parameter is a step
for i in range(0, 10, 2):
    print(i + 1)

name = "Reclaimer of his name"
for i in name:
    print(i)

for i in range(0, 20):
    if i == 13:
        continue
    else:
        print(i)
