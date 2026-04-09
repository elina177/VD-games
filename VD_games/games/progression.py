"""Игра: Арифметическая прогрессия"""

import random

GAME_RULE = 'What number is missing in the progression?'


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда"""
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    
    question = ' '.join(progression)
    return question, correct_answer
