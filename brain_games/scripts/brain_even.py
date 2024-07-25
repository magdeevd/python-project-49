#!/usr/bin/env python3 -u
import sys
from random import randint

import prompt


def is_even(number):
    return number % 2 == 0


def get_correct_answer(random_number):
    return 'yes' if is_even(random_number) else 'no'


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n')

    return name


def play_and_return_result():
    print('Answer "yes" if the number is even, otherwise answer "no".\n')

    for attempt in range(0, 3):
        random_number = randint(1, 100)
        correct_answer = get_correct_answer(random_number)
        answer = prompt.string(f'Question: {random_number} ')

        if answer == get_correct_answer(random_number):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            return False

    return True


def main():
    name = welcome_user()
    has_won = play_and_return_result()

    if has_won:
        print(f'\nCongratulations, {name}!')


if __name__ == '__main__':
    main()
