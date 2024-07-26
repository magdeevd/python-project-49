import random


def get_rule():
    return 'What number is missing in the progression?'


def generate_sequence():
    start = random.randint(1, 10)
    difference = random.randint(1, 10)

    sequence = [start + i * difference for i in range(random.randint(5, 10))]

    return sequence


def hide_one_number_in_sequence(sequence):
    replace_index = random.randint(0, len(sequence) - 1)
    hidden_number = sequence[replace_index]

    sequence[replace_index] = '..'

    return sequence, hidden_number


def generate_question():
    sequence, hidden_number = hide_one_number_in_sequence(generate_sequence())

    return f'Question: {' '.join(map(str, sequence))}', str(hidden_number)
