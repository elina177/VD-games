def welcome_user():
    """Приветствует пользователя и возвращает его имя"""
    print("Welcome to the VD-games!")
    
    name = input("May I have your name? ")
    
    while name.strip() == "":
        print("Name cannot be empty!")
        name = input("May I have your name? ")
    
    print(f"Hello, {name}!")
    return name
