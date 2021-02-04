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

while True:
    try:
        n = int(input("Введіть кількість чисел : "))
        operation = input("Виберіть операцію: +, -, *, /:  ")
        if operation == "+":
            result = 0
            i = 1
            while i <= n:
                number = int(input("Введіть число: "))
                result += number
                i += 1
            print(result)

        elif operation == "-":
            number = int(input("Введіть число: "))
            result = number
            i = 2
            while i <= n:
                number = int(input("Введіть число: "))
                result -= number
                i += 1
            print(result)

        elif operation == "*":
            result = 1
            i = 1
            while i <= n:
                number = int(input("Введіть число: "))
                result *= number
                i += 1
            print(result)

        elif operation == "/":
            number = int(input("Введіть число: "))
            result = number
            i = 1
            while i < n:
                number = int(input("Введіть число: "))
                try:
                    result /= number
                    i += 1
                except ZeroDivisionError:   
                    print("Ділення на 0 неможливе")          
            print(result)
            
        else:
            print("Введені дані не коректні")  

    except ValueError:
        print("Введено не коректні дані")

    if input("Continue? (Y/n) ") == "n":
        print("Bye!")
        break

