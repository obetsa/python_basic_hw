"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.

    1. При запуске, программа спрашивает имя игрока.

    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру

    3. При выходе из программы данные игрока записывать в файл (txt либо json).

    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.

"""

import random
def save():
    with open("save.txt", a) as f:
        

def magic():
    random_number = random.randint(1, 10)
    print(random_number)
    attempts = 0
    while attempts < 3:
        number = input("Введіть число: ")
        attempts += 1
        if int(number) > random_number:
            print("Введене число більше, за загадане")
        if int(number) < random_number:
            print("Введене число менше, за загадане")
        if int(number) == random_number:
            print(attempts, "спроби!", "Вгадали")
            # return magic()
        else:
            print("Використано", attempts, "спроби з трьох. Не вгадали")
            return magic()

    return magic()
    print("Введено не коректні дані")


magic()


# def game():

#     if input("Продовжити? (Y/n) ") == "n":
#         print("Bye!")
#         return
