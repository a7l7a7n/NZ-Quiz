""" Questions_v1
Asks the user questions asking 'what is the english word or runa or whatever'
"""


# Function
def user_answer(question_text):
    while True:
        question = input(question_text).lower()
        # If NZ, game starts
        if question == '14':
            print("Correct, Good job!")
        elif question == '18' or '13' or '17':
            print("Incorrect, tekau mā whā is 14")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'tekau mā whā?"
                    "a) 18\n"
                    "b) 13\n"
                    "c) 14\n"
                    "d) 17\n")
            return question


# Main Routine
questions_ = user_answer("What is the english number for 'tekau mā whā':\n"
                         "a) 18\n"
                         "b) 13\n"
                         "c) 14\n"
                         "d) 17\n:")
print(f"You have entered {questions_}")




