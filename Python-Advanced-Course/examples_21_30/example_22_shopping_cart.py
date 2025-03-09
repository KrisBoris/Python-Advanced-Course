# Example 22 - Shopping cart

foods = []
prices = []
total = 0.0

while True:
    item = input("Enter food to add to the list: ")
    if item.lower() == "q":
        break
    else:
        item_price = float(input("Enter food's price: "))
        foods.append(item)
        prices.append(item_price)
        total += item_price

print()
print(foods, end=", ")
print()
print(prices, end=", ")
print()
print(f"Total cost: ${total:.2f}")
