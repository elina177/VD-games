"""Игра: Калькулятор"""

import random

GAME_RULE = 'What is the result of the expression?'


def generate_round():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(operations)
    
    question = f"{num1} {operation} {num2}"
    
    if operation == '+':
        correct_answer = str(num1 + num2)
    elif operation == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    
    return question, correct_answer
