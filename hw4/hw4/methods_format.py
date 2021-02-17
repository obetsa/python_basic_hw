"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

# можно заменить данную строку на input()
string = 'Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY.'

# 1 пункт
count_upper = 0  # счетчик заглавных букв
count_lower = 0  # счетчик строчных букв

for char in string:  # проходим по строке и считаем строчные и заглавные буквы
    if char.isupper():
        count_upper += 1
    elif char.islower():
        count_lower += 1

if count_lower < count_upper:
    edited_string = string.upper()
elif count_lower > count_upper:
    edited_string = string.lower()
else:
    edited_string = string.swapcase()

print(
    f'1. Исходная строка: {string}.'
    f'\nРезультат: {edited_string}.'
)

# 2 пункт
if string.istitle():
    edited_string = 'done. ' + string
else:
    edited_string = 'draft. ' + string[5:]

print(
    f'2. Исходная строка: {string}.'
    f'\nРезультат: {edited_string}.'
)

# 3 пункт
if len(string) > 20:
    edited_string = string[:20]
else:
    edited_string = string.ljust(20, '@')

print(
    f'3. Исходная строка: {string}.'
    f'\nРезультат: {edited_string}.'
)

# Вместо f-строки можно написать 1 шаблон и использовать его.
template = '{}. Исходная строка: {}.\nРезультат: {}'

# тогда после каждого пункта будет вот такой принт
print(template.format('1', string, edited_string))
print(template.format('2', string, edited_string))
print(template.format('3', string, edited_string))
