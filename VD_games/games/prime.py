"""Игра: Простое число"""

import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда"""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
