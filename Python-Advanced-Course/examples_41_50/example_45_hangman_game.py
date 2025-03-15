# Example 45 - Hangman game

import random

hangman_img = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

words = ("apple", "banana", "blueberry", "pineapple", "coconut")


def show_hangman(wrong_answers):
    for row in range(len(hangman_img.get(wrong_answers))):
        print(f"{hangman_img.get(wrong_answers)[row]}")


def show_answer(answer):
    print(f"The answer is: {answer}")


def show_hint(hints):
    print(" ".join(hints))


def main():
    answer = random.choice(words)
    is_running = True
    wrong_answers = 0
    hints = ["_" for _ in answer]
    guessed_letters = set()

    while is_running:
        user_answer = input("Enter next letter: ")

        if len(user_answer) > 1 or not user_answer.isalpha():
            print("Invalid answer")
            continue

        if user_answer in guessed_letters:
            print("You already guessed that letter")
            continue

        if user_answer in answer:
            for index in range(len(answer)):
                if answer[index] == user_answer:
                    hints[index] = user_answer
        else:
            wrong_answers += 1

        guessed_letters.add(user_answer)
        show_hangman(wrong_answers)
        show_hint(hints)

        if wrong_answers >= 6:
            print("You lost!")
            show_answer(answer)
            is_running = False
        elif "_" not in hints:
            print("You won!")
            show_answer(answer)
            is_running = False


if __name__ == "__main__":
    main()