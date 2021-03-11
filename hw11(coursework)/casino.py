"""
    Casino

    ** для высшего балла хранить статистику игроков в файле
        и при каждом запуске casino запрашивать имя игрока.

    При запуске программы:
        - игроку необходимо ввести имя
        - попадаем в Главное меню
        * возможно у игрока должно быть изначально какое-то количество очков

    Главное меню:
    1. Magic
    2. Blackjack (21)
    3. Посмотреть статистику
    4. Сбросить игровой прогресс

    При выборе пункта 1.
        - выводятся правила игры
        - запускается игра magic (hw3/magic.py)
        - в игре ограниченное количество попыток
        * придумать правила начисления очков при угадывании с 1, 2 .. N попыток
        * придумать правила потери очков при проигрыше

    При выборе пункта 2.
        - выводятся правила игры
        - игрок делает ставку (не больше, чем у него имеется очков)
        - запускается игра blackjack (21)

    При выборе пункта 3.
        - выводится подробная статистика игрока:
            Имя игрока: Max
            Количество очков: 190

            Magic
            Всего игр сыграно: 20
            Выиграно: 5
            Коэффициент выигрышей: 0.25
            Рекордное количество попыток: 2

            Blackjack
            Всего игр сыграно: 0
            Выиграно: 0
            Коэффициент выигрышей: -

    При выборе пункта 4.
        - удаляются данные игрока
        - запрашивается имя нового игрока
        - попадаем в Главное меню


    Реализаци blackjack (правила https://en.wikipedia.org/wiki/Blackjack):
        - формируется колода карт
            от двойки до десятки — от 2 до 10 соответственно,
            у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1),
            у т.н. картинок (король, дама, валет) — 10.

            в итоге колода - [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

        - колода перетосовывается с помощью random.shuffle()
        - игроку предлагается на выбор:
            1. взять ещё карту
                - из колоды исключается одна карта и дается игроку
            2. остановиться

        - если у игрока в сумме выходит 21 - победа (игроку возвращается
         удвоенная ставка)
        - если у игрока в сумме выходит больше 21 (перебор) - проигрыш
         (ставка снимается в пользу казино)
        - если игрок остановился на сумме меньше 21 - ставка
         возвращается игроку

        * описынные выше правила можно дополнить по желанию
"""
import random
import json
from pathlib import Path

FILES_DIR = Path(__file__).resolve().parent / "files"
file_path = FILES_DIR / "casino.json"


class Casino:
    # можно указать атрибуты. Имя игрока, данные об играх и т.д.
    def __init__(self, name):
        self.name = name
        a = {}
        with open(file_path, "x") as f:
            a = json.dumps(a, indent=2)
        """
        Здесь создаем файл при инициализации, если его нет.
        Таким образом файл всегда будет существовать.
        """

    def launch(self):
        """ Запуск игры. Авторизация и переход в главное меню. """
        self.login()
        self.main_menu()

    def login(self):
        name = input("Enter your name: ")
        with open(file_path, "r") as f:
            name = json.load(f)
            if name == True:
                self.main_manu()
            else:
                return self.login()

        super().__init__(name)
                # with open(file_path, "a") as f:

        """
        Авторизация и запись информации об игроке.

        Пользователь вводит имя (input), по имени с файла получаем его данные.
        Если данных по такому имени не существует, то создаем их.

        После получения/создания записываем в атрибут класса.
        """

    def main_menu(self):
        user_choice = input('''Главное меню:
        1. Magic
        2. Blackjack (21)
        3. Посмотреть статистику
        4. Сбросить игровой прогресс''')
        if user_choice == "1":
            self.magic()
        elif user_choice == "2":
            blackjack()
        elif user_choice == "3":
            show_stat()
        elif user_choice == "4":
            reset()
        else:
            return main_menu()


    def magic(self):
    # Чтение файла (он должен существовать и быть валидным) и создание словаря
        default_data = {"games": 0, "record": None, "avg_attempts": 0}
        with open("users.json") as f:
            data = json.load(f)
            player_data = data.get(self.name, default_data)

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

                        # Перед выходом обновляем статистику игрока в файле
        with open(file_path, "r+") as f:
            data = json.load(f)
            data[self.name] = player_data
            data = json.dumps(data, indent=2)
            f.seek(0)
            f.write(data)
        """
        Здесь например будет какая-то игра.

        После каждой игры обновляем информацию о пользователе в атрибуте класса

        В конце возвращаем в главное меню либо выход из казино.
        """


    def some_game(self):
        """
        Здесь например будет какая-то игра.

        После каждой игры обновляем информацию о пользователе в атрибуте класса

        В конце возвращаем в главное меню либо выход из казино.
        """


    def __del__(self):
        """ При удалении обновляем информацию из атрибута в файле """




        if input("\nСгенерировать еще? (Y/n) ") != "n":
            return main()


def main():
    # Создаем объект класса Casino
    game = Casino()
    # Запускаем метод, который является точкой входа в игру
    game.launch()


if __name__ == "__main__":
    main()


