"""
    Определить, существует ли треугольник.

    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.

    * у треугольника каждая сторона меньше суммы двух других сторон
"""

# Solutions

# 1 вариант
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b > c and b + c > a and c + a > b:
    print("Triangle (", a, b, c, ") exists.")
else:
    print("Triangle (", a, b, c, ") does not exists.")

# 2 вариант
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
if a >= b + c:
    print("Not exist", a, b, c)
elif b >= a + c:
    print("Not exist", a, b, c)
elif c >= b + a:
    print("Not exist", a, b, c)
else:
    print("Exist", a, b, c)

# 3 вариант (с обработкой возможных ошибок)
a = input("a = ")
b = input("b = ")
c = input("c = ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print(a, b, c, "- invalid sides.")
else:
    if a < b + c and b < c + a and c < a + b:
        print("Triangle (", a, b, c, ") exists.")
    else:
        print("Triangle (", a, b, c, ") does not exists.")
