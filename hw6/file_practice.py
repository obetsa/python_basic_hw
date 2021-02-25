"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""
# with open("files/file_practice.txt", "w") as f:
#     print("Starting practice with files", file=f)

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

# with open("files/file_practice.txt", "r") as f:
#     f1 = f.read(5)
#     print(f1.upper())
#     f.seek(0)
#     print(f.read())

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

# with open("files/text.txt") as f:
#     text = f.read()
#     if text.count("i") > text.count("e"):
#         text = text.replace("i", "e")
#     else:
#         text = text.replace("e", "i")

# with open("file_practice.txt", "a") as f:
#     f.write(text)

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""

# with open("files/file_practice.txt", "a+") as f:
#     if len(f.read()) % 2 == 0:
#         f.write('\nthe end')
#         f.seek(0)
#         print(f.read())
#     else:
#         f.write('\nbye')
#         f.seek(0)
#         print(f.read())

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""

# with open("files/file_practice.txt", "r+") as f:
#     f1 = f.read()
#     print(f1)
#     c = len(f1)
#     x = c / 2
#     f.seek(x)
#     f.write(" *some inserted text* ")
