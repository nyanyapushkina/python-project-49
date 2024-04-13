from random import randint

RULES = 'What number is missing in the progression?'


def generate_progression():
    # Generate the number to start a progression with
    start_number = randint(0, 100)
    # Generate a step for an arithmetic progression
    progression_step = randint(1, 10)
    # Define the length of the progression, i.e the number of elements
    progression_length = randint(5, 10)

    progression = []

    i = 0
    # Fill the progression with all the numebers
    while i < progression_length:
        progression.append(str(start_number + progression_step * i))
        i += 1

    return progression


def hide_element(progression):
    # Extract one of the numbers and replace it with '..'
    hidden_number_index = randint(0, len(progression) - 1)
    hidden_element = progression[hidden_number_index]
    progression[hidden_number_index] = '..'
    # Add a whitespace after each element
    progression = ' '.join(progression)
    set = [hidden_element, progression]
    return set


def get_data():
    data = hide_element(generate_progression())
    progression = data[1]
    correct_answer = data[0]

    game_question = f'Question: {progression}'

    return game_question, str(correct_answer)
