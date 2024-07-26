import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n')

    return name


def play_three_rounds(rule, question_generator):
    print(f'{rule()}\n')

    for attempt in range(0, 3):
        question, correct_answer = question_generator()
        print(question)

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            return False

    return True


def start_game(rule, question_generator):
    name = welcome_user()
    has_won = play_three_rounds(rule, question_generator)

    if has_won:
        print(f'\nCongratulations, {name}!')
    else:
        print(f"\nLet's try again, {name}!")
