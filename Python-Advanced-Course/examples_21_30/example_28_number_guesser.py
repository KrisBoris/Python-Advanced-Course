# Example 28 - Random number guesser

import random

bottom_threshold = 1
upper_threshold = 100
answer = random.randint(bottom_threshold, upper_threshold)
is_running = True

while is_running:
    