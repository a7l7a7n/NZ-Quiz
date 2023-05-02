"""Want_To_Play_v1
This program asks the user if they want to play the Quiz
If yes, the game starts, if not then the program ends
"""


# function
def start(question_text):
    while True:
        play = input(question_text).lower()
        # If NZ, game starts
        if play == 'nz':
            print("Program starts")
            return play
        # Anything else
        else:
            print("Error")
            return play


# Main Routine:
play_ = start("Do you want to play the NZ Quiz?: ")
print()
