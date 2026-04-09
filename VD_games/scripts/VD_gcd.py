C:\Users\k-kuz\AppData\Local\Packages\MicrosoftWindows.Client.Core_cw5n1h2txyewy\TempState\ScreenClip\{624C46B2-8488-4B99-9B0F-64448641F280}.png
"""Точка входа для игры 'НОД'"""

from VD_games.games.gcd import generate_round, GAME_RULE
from VD_games.engine import run_game


def main():
    run_game(generate_round, GAME_RULE)


if __name__ == '__main__':
    main()
