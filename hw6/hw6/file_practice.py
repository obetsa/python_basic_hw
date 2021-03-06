"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""

with open("file_practice.txt", "w") as f:
    print("Starting practice with files", file=f)
    # or
    # f.write('Starting practice with files\n')

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

with open("file_practice.txt") as f:
    print(f.read(5).upper())
    f.seek(0)
    print(f.read())

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

with open("files/text.txt") as f:
    text = f.read()
    if text.count("i") > text.count("e"):
        text = text.replace("i", "e")
    else:
        text = text.replace("e", "i")

with open("file_practice.txt", "a") as f:
    f.write(text)

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""

with open("file_practice.txt", "a+") as f:
    f.seek(0)
    text = f.read()
    if len(text) % 2 == 0:
        f.write("the end")
    else:
        f.write("bye")

    f.seek(0)
    print(f.read())

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""

with open("file_practice.txt", "r+") as f:
    text = f.read()
    f.seek(0)
    center = len(text) // 2
    text = text[:center] + "*some inserted text*" + text[center:]
    f.write(text)
