
"""Точка входа для игры 'Простое число'"""

from VD_games.games.prime import generate_round, GAME_RULE
from VD_games.engine import run_game


def main():
    run_game(generate_round, GAME_RULE)


if __name__ == '__main__':
    main()
