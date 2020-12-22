"""
Главная функция. 
Создаёт функции-оператора из текста.
Работает только с внутренними функциями Питона.
"""

def func_create(func_name): #Не работает
    return exec(func_name)

if __name__ == "__main__":
    multi = func_create("__add__") 