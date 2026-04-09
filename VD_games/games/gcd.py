"""Игра: Наибольший общий делитель (НОД)"""

import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    """Находит НОД двух чисел"""
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(find_gcd(num1, num2))
    return question, correct_answer
