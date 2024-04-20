import prompt


def play(game):
    # Greet a player
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print(f'{game.RULES}')

    round = 0

    while round < 3:
        # Get data to ask a question and correct answer
        game_question, correct_answer = game.get_data()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        # Compare correct answer with the one provided by tthe player
        if user_answer != correct_answer:
            # If the player provides a wrong answer,
            # show the message and leave the game
            print(f"\'{user_answer}\' is wrong answer ;(. Correct answer was "
                  f"\'{correct_answer}\'.\nLet\'s try again, {name}!")
            break

        # If the player guessed correctly, show a message and continue
        print('Correct!')
        round += 1

    if round == 3:
        print(f'Congratulations, {name}!')
