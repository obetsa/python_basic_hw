"""
    Определить, существует ли треугольник.
    Программа принимает на ввод 3 стороны треугольника.
    Выводит стороны и текст, существует треугольник или нет.
    * у треугольника каждая сторона меньше суммы двух других сторон
"""

print("Введіть сторони трикутника")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Трикутник існує")
else:
    print("Трикутник не існує")