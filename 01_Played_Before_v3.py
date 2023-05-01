"""v2_Played_Before
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
            answer ='yes'
            print("Program continues")
        # If no, provide instructions
        elif answer == 'no' or answer == 'n':
            answer = 'no'
            print("Show instructions")
        # Else, re-enter question
        else:
            print("Please answer 'yes' or 'no'")
            print(yes_no("Have you played The NZ Quiz before?"))


#Main Routine:
answer = yes_no("Have you played The NZ Quiz before?: ")
print(f"You have entered '{answer}'")
print()
