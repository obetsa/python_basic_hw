"""
    Пример использования модулей random и string

    Программа выводит случайный спец-символ либо число.

    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

from random import choice
from string import digits, punctuation


def main():
    # генерируем строку для выборки
    tmp = digits + punctuation

    # выбираем случайный символ из строки
    char = choice(tmp)

    print(char)


main()
