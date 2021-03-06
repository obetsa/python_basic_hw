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
import json
import random


def main():
    # TODO: необходим рефакторинг этой функции

    name = input("Enter your name: ")

    # Чтение файла (он должен существовать и быть валидным) и создание словаря
    default_data = {"games": 0, "record": None, "avg_attempts": 0}
    with open("users.json") as f:
        data = json.load(f)
        player_data = data.get(name, default_data)

    # Здесь начинается игра
    random_number = random.randint(1, 10)
    counter = 0
    print("Guess the Magic number!\n")

    while True:

        try:
            number = int(input("The Magic number is "))
            counter += 1
        except ValueError:
            print("You must enter a number.")
            continue

        if number > random_number:
            print("No, the Magic number less than", number)
        elif number < random_number:
            print("No, the Magic number greater than", number)
        else:
            print("\nCongratulations! The Magic number is", number)
            print("Attempts:", counter)

            # При выигрыше обновляем информацию в player_data
            if not player_data["record"] or player_data["record"] > counter:
                player_data["record"] = counter

            games = player_data["games"]
            avg = player_data["avg_attempts"]

            player_data["games"] += 1
            player_data["avg_attempts"] = (games * avg + counter) / (games + 1)

            if input("\nContinue? (y/n) ") != "y":
                print("Bye!")
                break

            random_number = random.randint(1, 10)
            counter = 0

    # Перед выходом обновляем статистику игрока в файле
    with open("users.json", "r+") as f:
        data = json.load(f)
        data[name] = player_data
        data = json.dumps(data, indent=4)
        f.seek(0)
        f.write(data)


if __name__ == "__main__":
    main()
