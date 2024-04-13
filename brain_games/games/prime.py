from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    return d * d > number


def get_data():
    number_to_check = randint(0, 1000)
    game_question = f'Question: {number_to_check}'

    correct_answer = 'yes' if is_prime(number_to_check) else 'no'

    return game_question, correct_answer
