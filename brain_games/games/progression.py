from random import randint

RULES = 'What number is missing in the progression?'


def generate_progression(start_number, progression_step, progression_length):

    progression = []

    i = 0
    # Fill the progression with all the numebers
    while i < progression_length:
        progression.append(str(start_number + progression_step * i))
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
    start = randint(0, 100)
    # Generate a step for an arithmetic progression
    step = randint(1, 10)
    # Define the length of the progression, i.e the number of elements
    length = randint(5, 10)
    progression = generate_progression(start, step, length)
    hidden_number_index = randint(0, len(progression) - 1)

    correct_answer = progression[hidden_number_index]
    game_question = hide_element(progression, hidden_number_index)

    return game_question, str(correct_answer)
