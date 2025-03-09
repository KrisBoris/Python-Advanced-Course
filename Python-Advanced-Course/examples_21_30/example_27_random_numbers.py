# Example 27 - Random numbers

import random

# Random int between 1 and 20 inclusive
number = random.randint(1, 20)
print(number)
# Random float number between 0 and 1
number = random.random()
print(number)
# Picks random item from collection
options = ("rock", "paper", "scissors")
choice = random.choice(options)
# Shuffles given collection (works on original collection, not copy)
cards = ["8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
