"""
    (1-3 пункты были решены на уроке, необходимо привести все к нужному виду)

    При запуске программы выбор:
    1. Найти количество четных и нечетных цифр числа.
    2. Найти факториал числа.
    3. Вывести последовательность чисел в степени до предела.
    4. Выход.

    * после выполнения пунктов 1-3 попадаем обратно в меню.
"""


while True:
    choice = input(
        "Меню: \n"
        "1. Найти количество четных и нечетных цифр числа.\n"
        "2. Найти факториал числа.\n"
        "3. Вывести последовательность чисел в степени до предела.\n"
        "4. Выход.\n"
        "Сделайте выбор и нажмите Enter: "
    )
    if choice == "1":
        number = int(input("Ведите число: "))
        tmp = number
        even = 0
        odd = 0

        while number > 0:
            last_digit = number % 10

            if last_digit % 2 == 0:
                even += 1
            else:
                odd += 1

            number //= 10

        print("В числе", tmp, "четных цифр -", even, ", нечетных -", odd)
        print()

    elif choice == "2":
        number = int(input("Введите число, факториал которого найти: "))
        tmp = number
        factorial = 1
        while number > 1:
            factorial *= number
            number -= 1
        print("!", tmp, " = ", factorial, sep="")
        print()

    elif choice == "3":
        p = int(input("Введите степень: "))
        limit = int(input("Предел: "))
        number = 1

        while (result := number ** p) <= limit:
            print(result, end=" ")
            number += 1
        print()
        print()

    elif choice == "4":
        print("Bye!")
        break
