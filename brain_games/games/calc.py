from random import randint, choice

RULES = 'What is the result of the expression?'


def get_data():
    # Generate two random numbers, randomly choose
    # an operation type and create a question
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    operations_available = ['+', '-', '*']
    operation = choice(operations_available)

    game_question = f'Question: {number_1} {operation} {number_2}'

    # Correct answer depends on the chosen operation
    if operation == '+':
        correct_answer = number_1 + number_2

    elif operation == '-':
        correct_answer = number_1 - number_2

    elif operation == '*':
        correct_answer = number_1 * number_2

    return game_question, str(correct_answer)
