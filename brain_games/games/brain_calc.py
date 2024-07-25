import operator
import random


def get_rule():
    return 'What is the result of the expression?'


def generate_attempt_question():
    operators_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    first_operand = random.randint(1, 100)
    second_operand = random.randint(1, 100)
    operator_char = random.choice(['+', '-', '*'])

    correct_answer = operators_map[operator_char](first_operand, second_operand)

    return f'Question: {first_operand} {operator_char} {second_operand} ', str(correct_answer)
