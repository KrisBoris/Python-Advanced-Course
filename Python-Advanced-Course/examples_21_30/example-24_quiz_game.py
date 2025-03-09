# Example 24 - Quiz game

questions = ("How many elements are in the periodic table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in Earth's atmosphere?",
             "How many bones are in the human body?",
             "Which planet in the Solar System is the hottest?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Ostrich", "C. Platypus", "D. GMO Chicken"),
           ("A. Hydrogen", "B. Nitrogen", "C. Oxygen", "D. Carbon-Dioxide"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Merkury", "B. Venus", "C. Mars", "D. Jupiter"))

correct_answers = ("C", "B", "B", "A", "B")
answers = []
score = 0

for question in range(len(questions)):
    print(questions[question])
    for option in options[question]:
        print(option, end="   ")
    print()
    user_answer = input("Enter your answer: ").upper()
    answers.append(user_answer)

for i in range(len(correct_answers)):
    if answers[i] == correct_answers[i]:
        score += 1

print("\nCorrect answers are: ")
for answer in correct_answers:
    print(answer, end=", ")

print("\nYour answers were: ")
for answer in answers:
    print(answer, end=", ")

print(f"\nYour score is: {score * 100 / len(questions):.2f}%")