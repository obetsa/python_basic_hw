"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Введите строку: ')

# 1. 

s = string.split()
l = len(s)
print(l)

# 2. 

st = string.split()
count = 0
for i in st:
    if len(i) > count:
        count = len(i)
        word = i    
print(word)