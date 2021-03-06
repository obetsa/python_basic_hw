"""
    Магическое число.
    Необходимо угадать загаданное число за наименьшее количество попыток.
    Алгоритм:
    1. Генерируется случайное число.
    2. Пользователь вводит число.
    3. Если введенное число больше или меньше сгенерированного, то
        выводится соответствующее сообщение и возвращаемся к пункту 2.
    4. Иначе введенное число равняется сгенерированному -
        пользователь угадал число. Выводится само число и количество попыток.
        А так же вопрос "Continue? (Y/n) ".
    6. Если пользователь выбирает продолжить -
        обнуляем счетчик попыток и переходим к пункту 1.
    7. Иначе выводим сообщение 'Bye!'.
    * Для генерации случайного числа используем random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
    ** по желанию, можете хранить рекордное число попыток
    и сообщать пользователю, если он поставил новый рекорд
"""

import random
while True:
    try:
        random_number = random.randint(1, 10)  # случайное число от 1 до 10
        # print(random_number)
        attempts = 0
        while attempts < 3:

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
                print("Використано", attempts, "спроби з трьох. Не вгадали")

    except ValueError:
        print("Введено не коректні дані")

    if input("Продовжити? (Y/n) ") == "n":
        print("Bye!")
        break
