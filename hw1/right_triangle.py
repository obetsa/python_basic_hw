  
"""
    Вывести площадь и периметр прямоугольного треугольника.
    Катеты вводятся с помощью input().
    Площадь - произведение катетов деленное на 2.
    Периметр - сумма 3х сторон треугольника.
    * используйте теорему Пифагора: c ** 2 == a ** 2 + b ** 2
    * чтоб взять квадратный корень достаточно возвести в степень 0.5
"""

a = int(input('Катет a: '))
b = int(input('Катет b: '))
c = (a ** 2 + b ** 2)**(1/2)
p = (a + b + c)
print(c)
print(p)