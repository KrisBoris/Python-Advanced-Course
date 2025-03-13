# Example 30 - Dice roller

import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") ● ┌ ─ ┐ │ └ ┘

dice_img = {1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│ ●  ●  ● │",
                "│         │",
                "│ ●  ●  ● │",
                "└─────────┘")}

dices = []
total = 0

num_of_dices = input("Enter number of dices: ")
while not num_of_dices.isdigit():
    num_of_dices = input("Enter number of dices correctly: ")
num_of_dices = int(num_of_dices)

for i in range(num_of_dices):
    roll = random.randint(1, 6)
    dices.append(roll)
    total += roll

print(f"You score is {total}. Rolled dices: ")

for i in range(len(dice_img.get(1))):
    for j in range(num_of_dices):
        print((dice_img.get(dices[j]))[i], end="")
    print()
