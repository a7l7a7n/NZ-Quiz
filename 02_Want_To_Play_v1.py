"""Want_To_Play_v1
This program asks the user if they want to play the Quiz
If yes, the game starts, if not then the program ends
"""


# Function:
def yes_no(question_text):
    while True:
        # Ask user if they want to play
        answer = input(question_text).lower()
        # If they say yes, start game
        if answer == 'yes' or answer == 'y':
            answer = 'yes'
            print("Program continues")
        # If no, end program
        elif answer == 'no' or answer == 'n':
            answer = 'no'
            print("Ends program")
        # Else, re-enter question
        else:
            print("Please answer 'yes' or 'no'")
            print(yes_no("Have you played The NZ Quiz before?"))


# Main Routine:
answer = yes_no("Do you want to play the NZ Quiz?: ")
print(f"You have entered '{answer}'")
