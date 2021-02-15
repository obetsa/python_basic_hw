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

import string
import random


def main():
    print('''Виберіть пароль:
1 - легкий
2 - середній
3 - тяжкий
4 - пароль користувача''')
    choise_pass = int(input(''))
    if choise_pass == 1:
        l_password()
    elif choise_pass == 2:
        m_password()
    elif choise_pass == 3:
        s_password()
    elif choise_pass == 4:
        user_password()
    else:
        print('Невірні дані, спробуйти ще раз')
    return


def l_password():
    size = 8
    lowercase = (string.ascii_lowercase)
    light_p = "".join(random.sample(lowercase, size))
    print(light_p)


def m_password():
    size = 8
    lowercase = (string.ascii_lowercase)
    uppercase = (string.ascii_uppercase)
    number = (string.digits)
    middle = uppercase + lowercase + number
    middle_p = "".join(random.sample(middle, size))
    print(middle_p)


def s_password():
    size = random.randint(8, 16)
    lowercase = (string.ascii_lowercase)
    uppercase = (string.ascii_uppercase)
    number = (string.digits)
    symbols = (string.punctuation)
    strong = uppercase + lowercase + number + symbols
    strong_p = ''.join(random.sample(strong, size))
    print(strong_p)


def user_password():
    sumbols = input('Введіть символи з яких буде генеруватися пароль: ')
    size_p = int(input('Введіть довжину пароля: '))
    if size_p <= 8:
        print('Пароль не надійний')
    u_pass = "".join(random.sample(sumbols, size_p))
    print(u_pass)


if __name__ == '__main__':
    main()
