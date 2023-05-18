""" Final version
This code has the last versions of all the other components
"""

import random

# Maori numbers in a list
Maori_numbers = ["Kore", "Tahi", "Rua", "Toru", "Whā", "Rima", "Ono", "Whitu", "Waru", "Iwa",
                 "Tekau", "Tekau mā Tahi", "Tekau mā Rua", "Tekau mā Toru", "Tekau mā Whā",
                 "Tekau mā Rima", "Tekau mā Ono", "Tekau mā Whitu", "Tekau mā Waru", "Tekau mā Iwa",
                 "Rua Tekau"]
# The English number in a list
English_Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                   "18", "19", "20"]


# Function
def formatter(symbol, text):
    sides = symbol * 5
    formatter_text = f"{sides}, {text}, {sides}"
    top_bottom = symbol * len(formatter_text)
    return f"{top_bottom}\n{formatter_text}\n{top_bottom}"


# Function:
def yes_no(question_text):
    while True:
        # Ask user if they want to play
        answer = input(question_text).lower()
        # If they say yes, start game
        if answer == 'yes' or answer == 'y':
            answer = 'yes'
            print()
            return answer
        # If no, end program
        elif answer == 'no' or answer == 'n':
            answer = 'no'
            print()
            return answer
        # Else, re-enter question
        else:
            print("Please answer 'yes' or 'no'")
            yes_no("Do you want to play the NZ Quiz?")


# Function
def instructions():
    print()
    print("🥝🥝🥝🥝🥝 NZ Quiz Instructions 🥝🥝🥝🥝🥝\n"
          "The NZ Quiz is a 10 question quiz where you \n"
          "are asked questions regarding Maori number \n"
          "from 0 to 20")


# Function:
def yes_no_():
    while True:
        # Ask user if they have played before
        answer = instructions_.lower()
        # If they say yes, print instructions
        if answer == 'yes' or answer == 'y':
            print(instructions)
        # If no, program continues
        elif answer == 'no' or answer == 'n':
            print("Program continues")
        # Else, re-enter question
        else:
            print("Please answer 'yes' or 'no'")
            print(yes_no("Do you want to see the instructions to the NZ Quiz: "))


# function
def start(question_text):
    while True:
        play = input(question_text).lower()
        # If NZ, game starts
        if play == 'nz':
            print()
            return play
        # Anything else then the question is re - entered
        else:
            print("error, invalid input detected")
            print(start("Please enter 'NZ' to start: "))
            return play


# Asks the user 10 questions before game ends
def rounds():
    question = random.choice(Maori_numbers)
    attempt = input(f"What is the English number for {question}: ")
    # Finds out if the user is correct or not
    answer_index = Maori_numbers.index(question)
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

# Main routine
print(formatter("🥝", "Welcome to The NZ QUIZ for Kiwis"))
print()

answer_ = yes_no("Do you want to play the NZ Quiz?: ")
if answer_ == "no" or answer_ == "n":
    print("Goodbye, and have a good day")
    exit()

instructions_ = input("Do you want to see the instructions to the Quiz: ")
if instructions_ == "yes" or instructions_ == "y":
    instructions()
else:
    print()
play_ = start("Please enter 'NZ' to start: ")

for question_ in range(10):
    score += rounds()
print(formatter("🥝", f"Your final score in the NZ Quiz for Kiwis is {score} / 10"))
