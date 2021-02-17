"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

# Ниже описаны некоторые варианты решения задачи.

# 1 вариант
string = input("Enter a string: ")

counter = 0  # счетчик слов
word = ""  # переменная для текущего слова
longest_word = ""  # самое длинное слово

for char in string:
    if char.isalpha():
        # если встречается буква, добавляем ее к текущему слову
        word += char
    elif word:
        # если не буква и текущее слово не пустое
        counter += 1  # инкрементируем счетчик
        if len(word) > len(longest_word):
            # если длина текущего слова больше самого длинного - заменяем
            longest_word = word
        word = ""  # очищаем текущее слово
else:
    # этот блок выполнится после цикла. можем обработать последнее слово
    if word:
        counter += 1
        if len(word) > len(longest_word):
            longest_word = word

print("1.", counter)
print("2.", longest_word)


# 2 вариант (с регулярными выражениями)
import re

string = input("Enter a string: ")

words = re.findall(r"\w+", string)  # получаем список слов

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("1.", len(words))  # длина списка = количество слов
print("2.", longest_word)


# 3 вариант (темы следующих уроков)
string = input("Enter a string: ")

words = re.findall(r"\w+", string)  # получаем список слов
longest_word = max(words, key=len)  # получаем самое длинное слово из списка

print("1.", len(words))
print("2.", longest_word)
