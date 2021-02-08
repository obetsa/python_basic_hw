string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

r = string.replace(', ', ' ')
print(r)


# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53

i = r.rindex('s')
print(i)

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

l = r.lower()
c = l.count('i')
print(c)


# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)

f = r.find('simply dummy text')
print(f)
print(r[f: f + len('simply dummy text')])


# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

d = len(r) // 2 
print(d)
du = (r[:d] * 3) + r[d:]
print(du)
