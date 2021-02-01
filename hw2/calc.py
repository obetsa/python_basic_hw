"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.
    В зависимости от введенного оператора,
    между числами проводится определенная операция.
    Результат выводится на экран.
    * обработать все возможные ошибки программы с помощью try-except
"""
try:
    number_1 = int(input("Введіть перше число: "))
    operation = input('''Введіть символ:
+ додавання
- віднімання
* множення
/ ділення
''')
    number_2 = int(input("Введіть друге число: "))
    if operation == "+":
        print(number_1 + number_2)
    elif operation == "-":
        print(number_1 - number_2)
    elif operation == "*":
        print(number_1 * number_2)
    elif operation == "/":
        print(number_1 / number_2)
    else:
        print("Введені дані не коректні")
except ValueError:
    print("Введено не коректні дані")
except ZeroDivisionError:
    print("Ділення на 0 неможливе")