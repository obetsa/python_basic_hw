"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.

    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение нечетных чисел числового ряда.

    * обработать возможные ошибки
"""

start = input("Enter start: ")
end = input("Enter end: ")
try:
    start = int(start) if start else 0
    # start = int(start or 0)
    end = int(end)
except ValueError:
    print("Enter numbers.")
else:
    summ = 0
    for i in range(start, end + 1):
        summ += i
    print("1.", summ)

    mul = 1
    for i in range(start, end + 1):
        if i % 2 != 0:
            mul *= i
    print("2.", mul)

    # start = start + 1 if start % 2 else start
    # mul = 1
    # for i in range(start, end, 2):
    #     mul *= i
    # print("2.", mul)
