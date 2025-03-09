# Example 20 - Collections

fruits = ["apple", "banana", "blueberry", "avocado"]

print(fruits)
print(fruits[:3])

for fruit in fruits:
    print(fruit)

# print(help(fruit))
print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple"
# Appends at the end of list
fruits.append("strawberry")
fruits.remove("pineapple")
fruits.insert(0, "peach")
# Sorts in alphabetical order
fruits.sort()
fruits.reverse()
fruits.clear()
# Throws error if element is not in the list
# fruits.index("blueberry")

# Set (good for constants)
cars = {"Tesla", "Mercedes", "Fiat", "Tesla"}
cars.add("Toyota")
cars.remove("Fiat")
print(cars)
# Removes random object
cars.pop()
cars.clear()

# Duplicated objects are only printed once
print(cars)

# Tuple uses mostly the same functions as list
beverages = ("Water", "Apple juice", "Jack Daniels")
print(beverages.count("Water"))
for drink in beverages:
    print(drink)
