"""Played_Before_v3
This program is the third version that now make the code a while loop that can
only be broken by answering yes or no
"""


# Function:
def yes_no(question_text):
    while True:
        # Ask user if they have played before
        answer = input(question_text).lower()
        # If they say yes, skip instructions
        if answer == 'yes' or answer == 'y':
            answer = 'yes'
            print("Program continues")
            return answer
        # If no, provide instructions
        elif answer == 'no' or answer == 'n':
            answer = 'no'
            print("Show instructions")
            return answer
        # Else, re-enter question
        else:
            print("Please answer 'yes' or 'no'")
            print(yes_no("Do you want to see the instructions to the Quiz: "))


# Main Routine:
instructions = input("Do you want to see the instructions to the Quiz: ")
print(f"You have entered '{instructions}'")
print()
