"""v1_Played_Before
This program is the first version that asks the user if they have played before
"""

instructions = input("Have you played The NZ Quiz before? (Yes or No): ")

# If they say yes, skip instructions
if instructions == 'Yes':
    print("Program continues")

# If no, provide instructions
elif instructions == 'No':
    print("Provides Instructions")

# Else, re-enter question
else:
    print("re-enters question")
