"""
    Ввести с помощью input() 3 числа.
    Вывести их с помощью print() в обратном порядке.

    Пример работы программы:

    Ввод:
    1
    125
    13

    Вывод:
    13
    125
    1
"""

# Solutions

# 1.
a = input()
b = input()
c = input()

print(c)
print(b)
print(a)

# 2.
num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")
num_3 = input("Введите третье число: ")

print(num_3, num_2, num_1, sep="\n")
