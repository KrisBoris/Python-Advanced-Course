# Example 26 - Concession stand

menu = {"Popcorn": 6.99,
        "Nachos": 5.49,
        "Soda": 3.99,
        "Sweets": 2.99,
        "Water": 1.99}

cart = []
total = 0.0

while True:
    item = input("Pick an item (q to finish): ")
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        total += menu.get(item)

print(f"\nYour cart: {cart}")
print(f"Total price: ${total:.2f}")