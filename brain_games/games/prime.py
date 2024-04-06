from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_data():
    number_to_check = randint(0, 1000)
    game_question = f'Question: {number_to_check}'

    d = 2
    while d * d <= number_to_check and number_to_check % d != 0:
        d += 1
    if d * d > number_to_check:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return game_question, correct_answer
