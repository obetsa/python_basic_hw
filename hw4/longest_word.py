"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input('Введите строку: ')
count_a = 0
count_b = 0


# for char in string:
#     if char.isdigit():
#         count_a += 1

for char in string:
    if char == ' ':
        count_a +=1

# for chart in string:
#     if chart.index():
#         count_b +=1
#         print(chart)


print(count_a)
# print(count_b)
#print(s)


specials = ''
counter_d = counter_l = counter_u = 0

for char in string:
    if char.isdigit():
        counter_d += 1
    elif char.islower():
        counter_l += 1
    elif char.isupper():
        counter_u += 1
    elif not char.isspace():
        specials += char

print(counter_d, counter_l, counter_u)
print(specials)

