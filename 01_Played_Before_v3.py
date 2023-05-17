"""Played_Before_v3
This program is the third version that now make the code a while loop that can
only be broken by answering yes or no
"""


# Function
def instructions():
    print("🥝🥝🥝🥝🥝 NZ Quiz Instructions 🥝🥝🥝🥝🥝\n"
                "The NZ Quiz is a 10 question quiz where you \n"
                "are asked questions regarding Maori number \n"
                "from 0 to 20")


# Function:
def yes_no(question_text):
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


# Main Routine:
instructions_ = input("Do you want to see the instructions to the Quiz: ")
if instructions_ == "yes" or instructions_ == "y":
    instructions()
else:
    print()
