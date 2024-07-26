import math
import random


def get_rule():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    i = 3
    while i * i <= number and number % i != 0:
        i += 2

    return i * i > number


def generate_attempt_question():
    number = random.randint(1, 100)

    correct_answer = 'yes' if is_prime(number) else 'no'

    return f'Question: {number}', str(correct_answer)
