"""Want_To_Play_v3
This program fixes the problems in the last version
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
play_ = start("Please enter 'NZ' to start: ")
print(f"You have entered '{play_}'")
