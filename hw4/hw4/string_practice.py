string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

string = string.replace(',', '')
# or
# string = string.replace(', ', ' ')

print('1.', string)

# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53

idx = string.rindex('s')

# or
# idx = string.rfind('s')

print('2.', idx)

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

count = string.lower().count('i')

print('3.', count)

# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)

start_idx = string.index('simply')
end_idx = string.index('text') + len('text')

# or
# start_idx = string.index('simply dummy text')
# end_idx = start_idx + len('simply dummy text')

print('4.', string[start_idx:end_idx])

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

center = len(string) // 2

print('5.', string[:center] * 3 + string[center:])
