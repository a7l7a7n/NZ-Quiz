""" Questions_v3
This code is the continuation of the last version. It now has a scoring system allowing the user to see how many
 questions out of ten they got.
"""

import random

# Maroi numbers in a list
Maroi_numbers = ["Kore", "Tahi", "Rua", "Toru", "Whā", "Rima", "Ono", "Whitu", "Waru", "Iwa",
                 "Tekau", "Tekau mā Tahi", "Tekau mā Rua", "Tekau mā Toru", "Tekau mā Whā",
                 "Tekau mā Rima", "Tekau mā Ono", "Tekau mā Whitu", "Tekau mā Waru", "Tekau mā Iwa",
                 "Rua Tekau"]
# The English number in a list
English_Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                   "18", "19", "20"]


# Function
# Asks the user 10 questions before game ends
def rounds():
    question = random.choice(Maroi_numbers)
    attempt = input(f"What is the English number for {question}: ")
    # Finds out if the user is correct or not
    answer_index = Maroi_numbers.index(question)
    answer = English_Numbers[answer_index]
    # Users score
    user_score = 0

    # Printing users results
    if attempt == answer:
        user_score += 1
        print("🥝🥝🥝Correct, Good Job!🥝🥝🥝")

    else:
        print("🥝🥝🥝Incorrect, Good try though!🥝🥝🥝")

    return user_score


score = 0
for question_ in range(10):
    score += rounds()


# Main routine
print(f"Your final score in the NZ Quiz for Kiwis is {score} / 10")
