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

# Solutions

x = int(input("x = "))
y = int(input("y = "))

# 1
if x > 0 and y > 0:
    print("I quarter")
elif x < 0 and y > 0:
    print("II quarter")
elif x < 0 and y < 0:
    print("III quarter")
elif x > 0 and y < 0:
    print("IV quarter")
else:
    print("On the coordinate system axis")

# 2
if x > 0:
    if y > 0:
        print("I")
    elif y < 0:
        print("IV")
elif x < 0:
    if y > 0:
        print("II")
    elif y < 0:
        print("III")
