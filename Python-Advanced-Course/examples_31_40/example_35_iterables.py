# Example 35 - Iterables

dictionary = {"A": 1, "B": 2, "C": 3}

for item in dictionary.values():
    print(item)

for key, value in dictionary.items():
    print(f"{key} = {value}", end="   ")