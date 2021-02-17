"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""

# Solutions

while True:
    # здесь нужно обрабатывать ValueError
    n = int(input("Сколько будет чисел? "))
    op = input("(+, -, *, /) ")

    result = 1
    for i in range(n):
        # здесь нужно обрабатывать ValueError
        number = int(input("Введите число: "))
        # number = int(input(f'Введите {i + 1} число: '))  # с номером числа

        if result is None:  # если result пустой - записываем в него 1 число
            result = number
        elif op == "+":
            result += number
        elif op == "-":
            result -= number
        elif op == "*":
            result *= number
        elif op == "/":
            # здесь нужно обработать деление на 0
            result /= number

    print("Результат:", result)

    if input("Continue? (y/n) ") != "y":
        print("Bye!")
        break


# while True:
#     try:
#         n = int(input("Введіть кількість чисел : "))
#         operation = input("Виберіть операцію: +, -, *, /:  ")
#         if operation == "+":
#             result = 0
#             i = 1
#             while i <= n:
#                 number = int(input("Введіть число: "))
#                 result += number
#                 i += 1
#             print(result)

#         elif operation == "-":
#             number = int(input("Введіть число: "))
#             result = number
#             i = 2
#             while i <= n:
#                 number = int(input("Введіть число: "))
#                 result -= number
#                 i += 1
#             print(result)

#         elif operation == "*":
#             result = 1
#             i = 1
#             while i <= n:
#                 number = int(input("Введіть число: "))
#                 result *= number
#                 i += 1
#             print(result)

#         elif operation == "/":
#             number = int(input("Введіть число: "))
#             result = number
#             i = 1
#             while i < n:
#                 number = int(input("Введіть число: "))
#                 try:
#                     result /= number
#                     i += 1
#                 except ZeroDivisionError:
#                     print("Ділення на 0 неможливе")
#             print(result)

#         else:
#             print("Введені дані не коректні")

#     except ValueError:
#         print("Введено не коректні дані")

#     if input("Continue? (Y/n) ") == "n":
#         print("Bye!")
#         break
