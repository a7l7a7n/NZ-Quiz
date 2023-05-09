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
        # If the user guesses 19 they are right otherwise they are wrong or have to re-enter the question
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
        # If the user guesses 2 they are right otherwise they are wrong or have to re-enter the question
        if question3 == '2':
            print("Correct, Good job!")
        elif question3 == '1' or '3' or '4':
            print("Incorrect, rua is 2")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'rua?"
                    "a) 1\n"
                    "b) 2\n"
                    "c) 3\n"
                    "d) 4\n")
            return question3


def user_answer_4(question_text):
    while True:
        question4 = input(question_text).lower()
        # If the user guesses 10 they are right otherwise they are wrong or have to re-enter the question
        if question4 == '10':
            print("Correct, Good job!")
        elif question4 == '9' or '8' or '7':
            print("Incorrect, tekau is 10")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'tekau?"
                    "a) 10\n"
                    "b) 9\n"
                    "c) 8\n"
                    "d) 7\n")
            return question4


def user_answer_5(question_text):
    while True:
        question5 = input(question_text).lower()
        # If the user guesses 7 they are right otherwise they are wrong or have to re-enter the question
        if question5 == '7':
            print("Correct, Good job!")
        elif question5 == '9' or '8' or '6':
            print("Incorrect, whitu is 7")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'whitu'?"
                    "a) 9\n"
                    "b) 8\n"
                    "c) 7\n"
                    "d) 6\n")
            return question5


def user_answer_6(question_text):
    while True:
        question6 = input(question_text).lower()
        # If the user guesses 12 they are right otherwise they are wrong or have to re-enter the question
        if question6 == '12':
            print("Correct, Good job!")
        elif question6 == '11' or '13' or '14':
            print("Incorrect, tekau mā rua  is 12")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'tekau mā rua'?"
                    "a) 11\n"
                    "b) 12\n"
                    "c) 13\n"
                    "d) 14\n")
            return question6


def user_answer_7(question_text):
    while True:
        question7 = input(question_text).lower()
        # If the user guesses 5 they are right otherwise they are wrong or have to re-enter the question
        if question7 == '5':
            print("Correct, Good job!")
        elif question7 == '4' or '3' or '6':
            print("Incorrect, rima is 5")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'rime'?"
                    "a) 3\n"
                    "b) 4\n"
                    "c) 5\n"
                    "d) 6\n")
            return question7


def user_answer_8(question_text):
    while True:
        question8 = input(question_text).lower()
        # If the user guesses 0 they are right otherwise they are wrong or have to re-enter the question
        if question8 == '0':
            print("Correct, Good job!")
        elif question8 == '1' or '3' or '2':
            print("Incorrect, kore is 0")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'kore'?"
                    "a) 0\n"
                    "b) 1\n"
                    "c) 2\n"
                    "d) 3\n")
            return question8
def user_answer_9(question_text):
    while True:
        question9 = input(question_text).lower()
        # If the user guesses 15 they are right otherwise they are wrong or have to re-enter the question
        if question9 == '15':
            print("Correct, Good job!")
        elif question9 == '11' or '13' or '17':
            print("Incorrect, tekau mā rima is 15")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'tekau mā rima'?"
                    "a) 11\n"
                    "b) 13\n"
                    "c) 15\n"
                    "d) 17\n")
            return question9
def user_answer_10(question_text):
    while True:
        question10 = input(question_text).lower()
        # If the user guesses 3 they are right otherwise they are wrong or have to re-enter the question
        if question10 == '3':
            print("Correct, Good job!")
        elif question10 == '11' or '13' or '17':
            print("Incorrect, toru is 3")
        else:
            print("Invalid number, please try again")
            print("What is the english number for 'toru'?"
                    "a) 1\n"
                    "b) 3\n"
                    "c) 5\n"
                    "d) 7\n")
            return question10


# Main Routine
questions_ = user_answer_1("What is the english number for 'tekau mā whā':\n"
                            "a) 18\n"
                            "b) 13\n"
                            "c) 14\n"
                            "d) 17\n")
print(f"You have entered {questions_}")
questions_2 = user_answer_2("What is the english number for 'tekau mā iwa':\n"
                            "a) 19\n"
                            "b) 18\n"
                            "c) 17\n"
                            "d) 16\n")
print(f"You have entered {questions_2}")
questions_3 = user_answer_3("What is the english number for 'rua':\n"
                            "a) 1\n"
                            "b) 2\n"
                            "c) 3\n"
                            "d) 4\n")
print(f"You have entered {questions_3}")
questions_4 = user_answer_4("What is the english number for 'tekau':\n"
                            "a) 10\n"
                            "b) 9n"
                            "c) 8\n"
                            "d) 7\n")
print(f"You have entered {questions_4}")
questions_5 = user_answer_5("What is the english number for 'whitu':\n"
                            "a) 9\n"
                            "b) 8\n"
                            "c) 7\n"
                            "d) 6\n")
print(f"You have entered {questions_5}")
questions_6 = user_answer_6("What is the english number for 'tekau mā rua':\n"
                            "a) 11\n"
                            "b) 12\n"
                            "c) 13\n"
                            "d) 14\n")
print(f"You have entered {questions_6}")
questions_7 = user_answer_7("What is the english number for 'rima':\n"
                            "a) 3\n"
                            "b) 4\n"
                            "c) 5\n"
                            "d) 6\n")
print(f"You have entered {questions_7}")
questions_8 = user_answer_8("What is the english number for 'kore':\n"
                            "a) 0\n"
                            "b) 1\n"
                            "c) 2\n"
                            "d) 3\n")
print(f"You have entered {questions_8}")
questions_9 = user_answer_9("What is the english number for 'tekau mā rima':\n"
                            "a) 11\n"
                            "b) 13\n"
                            "c) 15\n"
                            "d) 17\n")
print(f"You have entered {questions_9}")
questions_10 = user_answer_10("What is the english number for 'toru':\n"
                                "a) 1\n"
                                "b) 3\n"
                                "c) 5\n"
                                "d) 7\n")
print(f"You have entered {questions_10}")
