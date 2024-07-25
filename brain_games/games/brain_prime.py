import math
import random


def get_rule():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def generate_attempt_question():
    number = random.randint(1, 100)

    correct_answer = 'yes' if is_prime(number) else 'no'

    return f'Question: {number}', str(correct_answer)
