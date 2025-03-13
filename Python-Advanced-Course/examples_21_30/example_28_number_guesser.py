# Example 28 - Random number guesser

import random

bottom_threshold = 1
upper_threshold = 100
answer = random.randint(bottom_threshold, upper_threshold)
guesses = 0
is_running = True

while is_running:
    user_answer = input("Enter your answer: ")
    if user_answer.isdigit():
        user_answer = int(user_answer)
        guesses += 1
        if user_answer > answer:
            print("Your answer is too HIGH")
        elif user_answer < answer:
            print("Your answer is too LOW")
        else:
            print(f"Correct. The right answer was: {answer}")
            print(f"It took you {guesses} guesses")
            is_running = False
    else:
        print("Incorrect data type. Try again.")
