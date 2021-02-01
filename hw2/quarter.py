  
"""
    Программа принимает на ввод координаты точки - x и y.
    Выводит, в какой четверти системы координат лежит точка.
                ^ y
                |
            II  |    I
                |
        --------=-------->
                |         x
            III |    IV
                |
"""

x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("1")
elif x > 0 and y < 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x < 0 and y > 0:
    print("4")
elif x == 0 or y == 0:
    print("Точка в центрі або на осі")
else:
    print("Координати введено невірно")