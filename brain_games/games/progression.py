from random import randint

RULES = 'What number is missing in the progression?'

FIRST_TERM_MIN = 0
FIRST_TERM_MAX = 100

COMMON_DIFFERENCE_MIN = 1
COMMON_DIFFERENCE_MAX = 10

NUMBER_OF_TERMS_MIN = 5
NUMBER_OF_TERMS_MAX = 10


def generate_progression(first_term, common_difference, number_of_terms):

    progression = []

    i = 0
    # Fill the progression with all the numebers
    while i < number_of_terms:
        progression.append(str(first_term + common_difference * i))
        i += 1

    return progression


def hide_element(progression, hidden_number_index):
    # Extract one of the numbers and replace it with '..'
    progression[hidden_number_index] = '..'
    # Add a whitespace after each element
    progression = ' '.join(map(str, progression))
    return progression


def get_data():
    # Generate the number to start a progression with
    first_term = randint(FIRST_TERM_MIN, FIRST_TERM_MAX)
    # Generate a step for an arithmetic progression
    common_difference = randint(COMMON_DIFFERENCE_MIN, COMMON_DIFFERENCE_MAX)
    # Define the length of the progression, i.e the number of elements
    number_of_terms = randint(NUMBER_OF_TERMS_MIN, NUMBER_OF_TERMS_MAX)
    progression = generate_progression(first_term, common_difference,
                                       number_of_terms)
    hidden_number_index = randint(0, len(progression) - 1)

    correct_answer = progression[hidden_number_index]
    game_question = hide_element(progression, hidden_number_index)

    return game_question, str(correct_answer)
