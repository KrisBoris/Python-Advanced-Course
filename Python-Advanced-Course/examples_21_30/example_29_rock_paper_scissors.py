# Example 29 - Rock, paper, scissors game

import random

choices = ("rock", "paper", "scissors")
is_running = True
score = 0
games = 0

while is_running:
    choice = random.choice(choices)
    user_choice = input("Enter your choice: ")
    while user_choice not in choices:
        user_choice = input("Enter either rock, paper or scissors: ")
    games += 1

    if (user_choice == "rock" and choice == "rock"
        or user_choice == "paper" and choice == "paper"
        or user_choice == "scissors" and choice == "scissors"):

        print(f"Computer choose {choice}. It's a tie!")

    elif (user_choice == "rock" and choice == "paper"
          or user_choice == "paper" and choice == "scissors"
          or user_choice == "scissors" and choice == "rock"):

        print(f"Computer choose {choice}. You lose!")

    else:
        print(f"Computer choose {choice}. You win!")
        score += 1

    if not input("Would you like to play again (Y to play)? ").lower() == "y":
        print(f"You won {score} games out of {games}\nThanks for playing!")
        is_running = False
