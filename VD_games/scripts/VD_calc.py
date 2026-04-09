
"""Точка входа для игры 'Калькулятор'"""

from VD_games.games.calc import generate_round, GAME_RULE
from VD_games.engine import run_game


def main():
    run_game(generate_round, GAME_RULE)


if __name__ == '__main__':
    main()
