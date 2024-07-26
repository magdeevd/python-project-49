import operator
import random


def get_rule():
    return 'What is the result of the expression?'


def generate_question():
    operators_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    o = random.choice(['+', '-', '*'])

    correct_answer = operators_map[o](num_1, num_2)

    return f'Question: {num_1} {o} {num_2} ', str(correct_answer)
