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


def game():
    random_number = random.randint(1, 10)
    # print(random_number)
    attempts = 0
    while True:
        try:
            number = int(input("Введіть число: "))
            attempts += 1
            if number > random_number:
                print("Введене число більше, за загадане")
            if number < random_number:
                print("Введене число менше, за загадане")
            if number == random_number:
                print(attempts, "спроби!", "Вгадали")
                break
            else:
                print("Використано", attempts, "спроби. Не вгадали")
        except ValueError:
            print("Введено не коректні дані")
    return attempts


def save(stats):
    with open('save.txt', 'a+') as f:
        f.write(f'{stats}\n')


def menu():
    stats = {}
    games = 0
    record = []
    avg_attempts = 0
    sum_attempts = 0
    name = input("Enter Name: ")
    while True:
        attempts = game()
        sum_attempts += attempts
        games += 1
        avg_attempts = sum_attempts / games
        record.append(attempts)
        if input("Продовжити? (Y/n) ") == "n":
            stats['name'] = name
            stats['games'] = games
            stats['record'] = min(record)
            stats['avg_attempts'] = avg_attempts
            return stats
            print("Bye!")
            break


def main():
    stats = menu()
    save(stats)


main()
