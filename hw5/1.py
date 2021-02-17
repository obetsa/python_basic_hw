"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)

    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)


    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501
import random

from string import ascii_lowercase, ascii_letters, digits, punctuation


def main():
    choice = input(
        "1. Сгенерировать простой пароль\n"
        "2. Сгенерировать средний пароль\n"
        "3. Сгенерировать сложный пароль\n"
    )
    if choice == "1":
        # password = gen_simple_pw()
        password = gen_password(ascii_lowercase)
    elif choice == "2":
        password = gen_password(ascii_letters + digits)
        # password = gen_medium_pw()
    elif choice == "3":
        password = gen_strong_pw()

    print(password)


# def gen_simple_pw():
#     password = ""
#     for i in range(8):
#         password += random.choice(ascii_lowercase)
#     return password
#     # return "".join(random.sample(ascii_lowercase, 8))


# def gen_medium_pw():
#     password = ""
#     for i in range(8):
#         password += random.choice(ascii_letters + digits)
#     return password


def gen_password(chars, length=8):
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


def gen_strong_pw():
    length = random.randint(8, 16)
    password = gen_password(digits + ascii_letters + punctuation, length)

    counter_d = counter_u = counter_l = counter_s = 0
    for char in password:
        if char.isdigit():
            counter_d += 1
        elif char.isupper():
            counter_u += 1
        elif char.islower():
            counter_l += 1
        elif not char.isspace():
            counter_s += 1

    if counter_d and counter_u and counter_l and counter_s:
        return password
    return gen_strong_pw()


if __name__ == "__main__":
    main()