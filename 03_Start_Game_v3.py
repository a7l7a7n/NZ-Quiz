"""Start game v3
This code makes sure that if the user doesn't enter a valid input, the question is re - entered
"""


# function
def start(question_text):
    while True:
        play = input(question_text).lower()
        # If NZ, game starts
        if play == 'nz':
            print("Program starts")
            return play
        # Anything else then the question is re - entered
        else:
            print("error, invalid input detected")
            print(start("Please enter 'NZ' to start: "))
            return play


# Main Routine:
play_ = start("Please enter 'NZ' to start: ")
print(f"You have entered '{play_}'")
