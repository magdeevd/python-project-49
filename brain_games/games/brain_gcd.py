import random


def get_rule():
    return 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_question():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    correct_answer = gcd(first_number, second_number)

    return f'Question: {first_number} {second_number}', str(correct_answer)
