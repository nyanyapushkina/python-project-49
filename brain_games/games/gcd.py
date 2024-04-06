from random import randint
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'


def get_data():
    # Generate two random numbers and create a question
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)

    game_question = f'Question: {number_1} {number_2}'

    correct_answer = str(gcd(number_1, number_2))

    return game_question, correct_answer
