"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"

"""
import re


def frequent_word(text):
    # получаем все слова из текста (данная регулярка работает только для англ)
    words = re.findall(r"[a-zA-Z]+", text)
    # сортируем по алфавиту, чтоб выполнить условие с приоритетом
    words = sorted(words, key=str.lower)

    # вместо словаря можно использовать 2 переменные либо другую коллекцию
    tmp_dict = {"word": "", "count": 0}
    for word in words:
        if words.count(word) > tmp_dict["count"]:
            tmp_dict = {"word": word, "count": words.count(word)}
    return tmp_dict["word"]


text = "red, blue, yellow, red, blue, green, yellow, black"
assert frequent_word(text) == "blue"

text = "hi world, hi python. i am very cool but i am still learning."
assert frequent_word(text) == "am"

print("tests passed")
