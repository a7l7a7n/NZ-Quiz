"""Want_To_Play_v3
This program adds another function to improve the overall outcome of the program
"""


# function
def start(question_text):
    while True:
        play = input(question_text).lower()
        # If NZ, game starts
        if play == 'nz':
            print("Program starts")
        # Anything else
        else:
            print("Error")


# Main Routine:
play_ = start("Please enter 'NZ' to start: ")
print(f"You have entered '{play_}'")
