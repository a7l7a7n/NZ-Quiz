""" Questions_v1
Asks the user a random Question out of Maroi number 1 - 20
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
# Asks the user a question
question = random.choice(Maroi_numbers)
attempt = input(f"What is the English number for {question}: ")

# Finds out if the user is correct or not
answer_index = Maroi_numbers.index(question)
answer = English_Numbers[answer_index]

# Printing users results
if attempt == answer:
    print("🥝🥝🥝Correct, Good Job!🥝🥝🥝")

else:
    print("🥝🥝🥝Incorrect, Good try though!🥝🥝🥝")

