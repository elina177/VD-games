
"""Точка входа для игры 'Проверка на чётность'"""

from VD_games.engine import run_game
from VD_games.games.even import GAME_RULE, generate_round


def main():
    run_game(generate_round, GAME_RULE)


if __name__ == '__main__':
    main()
