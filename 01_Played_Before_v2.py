"""v2_Played_Before
This program is the second version that changes the code to allow for 'n' and 'y' to be used
instead of yes or no
"""

instructions = input("Have you played The NZ Quiz before? (Yes or No): ")

# If they say yes, skip instructions
if instructions == 'Yes' or instructions == 'y':
    print("Program continues")

# If no, provide instructions
elif instructions == 'No' or instructions == 'n':
    print("Provides Instructions")

# Else, re-enter question
else:
    print("re-enters question")
