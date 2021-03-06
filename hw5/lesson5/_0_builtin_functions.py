"""
    В python 60+ встроенных функций (см. презентацию 5 урока.)
"""

# abs(n) - возвращает число n по модулю
print(abs(-10))  # 10

# min(*args) - возвращает минимальный элемент последовательности
print(min(6, 3, -1, 17, -3.14, 0))  # -3.14

# max(*args) - возвращает максимальный элемент последовательности
print(max(6, 3, -1, 17, -3.14, 0))  # 17

# pow(x, y) - возвращает x в степени y
print(pow(2, 3))  # 8

# round(x, n) - возвращает число x округленное до n знаков после запятой
print(round(3.141592653589793, 2))  # 3.14

# eval(string) - выполняет переданную строку как python код
eval('print(2 + 2)')  # 4

# dir(obj) - возвращает список доступных методов
print(dir(str))  # выведет все методы строки
print(dir('abc'))  # выведет все методы строки

# help(func) - отображает описание (докстринг) функции (метода)
help('abc'.lower)  # выведет описание строчного метода lower (для выхода - q)