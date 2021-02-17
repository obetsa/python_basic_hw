"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.

    В зависимости от введенного оператора,
    между числами проводится определенная операция.

    Результат выводится на экран.

    * обработать все возможные ошибки программы с помощью try-except
"""

# Solutions

# 1 вариант (все в try-except)
try:
    a = int(input("a = "))
    op = input("(+, -, *, /): ")
    b = int(input("b = "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "**":
        result = a ** b
    elif op == "/":
        result = a / b
    else:
        result = "only operations +, -, *, / are available"
except ValueError:
    print("You must enter a number!")
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Result:", result)

# 2 вариант (деление на 0 обрабатывается с помощью if-else)
try:
    a = int(input("a = "))
    op = input("(+, -, *, /): ")
    b = int(input("b = "))
except ValueError:
    print("You must enter a number!")
else:
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "**":
        result = a ** b
    elif op == "/":
        result = a / b if b != 0 else "division by zero"
        # or classic
        # if b != 0:
        #     result = a / b
        # else:
        #     result = "division by zero"
    else:
        result = "only operations +, -, *, / are available"

    print("Result:", result)
