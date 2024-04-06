from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_data():
    # Generate a random number and create a question
    number_to_check = randint(0, 1000)
    game_question = f'Question: {number_to_check}'

    # If the number is exactly divisible by 2, it is even
    correct_answer = 'yes' if number_to_check % 2 == 0 else 'no'
    return game_question, correct_answer
