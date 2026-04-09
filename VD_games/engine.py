"""Движок для запуска игр"""


def run_game(generate_round_func, game_rule):
    """Запускает игру: 3 раунда, проверка ответов"""
    from VD_games.cli import welcome_user
    
    print(game_rule)
    name = welcome_user()
    
    rounds_to_win = 3
    
    for _ in range(rounds_to_win):
        question, correct_answer = generate_round_func()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
