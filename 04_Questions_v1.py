""" Questions_v1
Asks the user questions 1 -10 asking 'what is the english word or runa or whatever'
"""


# Function
def user_answer_1(question_text):
    while True:
        question = input(question_text).lower()
        # If the user guesses 14 they are right otherwise they are wrong or have to re-enter the question
        if question == '14':
            print("Correct, Good job!")
        elif question == '18' or '13' or '17':
            print("Incorrect, tekau mā whā is 14")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'tekau mā whā?"
                    "a) 18\n"
                    "b) 17\n"
                    "c) 14\n"
                    "d) 13\n")
            return question


def user_answer_2(question_text):
    while True:
        question2 = input(question_text).lower()
        # If the user guesses 14 they are right otherwise they are wrong or have to re-enter the question
        if question2 == '19':
            print("Correct, Good job!")
        elif question2 == '18' or '16' or '17':
            print("Incorrect, tekau mā iwa is 19")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'tekau mā iwa?"
                    "a) 19\n"
                    "b) 18\n"
                    "c) 17\n"
                    "d) 16\n")
            return question2


def user_answer_3(question_text):
    while True:
        question3 = input(question_text).lower()
        # If the user guesses 14 they are right otherwise they are wrong or have to re-enter the question
        if question3 == '2':
            print("Correct, Good job!")
        elif question3 == '1' or '3' or '4':
            print("Incorrect, rua is 2")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'tekau mā iwa?"
                    "a) 1\n"
                    "b) 2\n"
                    "c) 3\n"
                    "d) 4\n")
            return question3


# Main Routine
questions_ = user_answer_1("What is the english number for 'tekau mā whā':\n"
                            "a) 18\n"
                            "b) 13\n"
                            "c) 14\n"
                            "d) 17\n:")
print(f"You have entered {questions_}")
questions_2 = user_answer_2("What is the english number for 'tekau mā iwa':\n"
                            "a) 19\n"
                            "b) 18\n"
                            "c) 17\n"
                            "d) 16\n:")
print(f"You have entered {questions_2}")
questions_3 = user_answer_2("What is the english number for 'rua':\n"
                            "a) 1\n"
                            "b) 2\n"
                            "c) 3\n"
                            "d) 4\n")
print(f"You have entered {questions_3}")
