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


def hide_element(line):
    # Extract one of the numbers and replace it with '..'
    hidden_number_index = randint(0, line - 1)
    hidden_element = line[hidden_number_index]
    line[hidden_number_index] = '..'
    # Add a whitespace after each element
    line = ' '.join(line)
    set = [hidden_element, line]
    return set


def get_data():
    data = hide_element(generate_progression())
    progression = data[1]
    correct_answer = data[0]

    game_question = f'Question: {progression}'

    return game_question, str(correct_answer)
