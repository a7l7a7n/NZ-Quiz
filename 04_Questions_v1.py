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
English_Numbers = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                   "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                   "Eighteen", "Nineteen", "Twenty"]

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

