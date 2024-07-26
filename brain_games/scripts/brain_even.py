#!/usr/bin/env python3
from brain_games.games.brain_even import get_rule, generate_question
from brain_games.games.core import start_game


def main():
    start_game(get_rule, generate_question)


if __name__ == '__main__':
    main()
