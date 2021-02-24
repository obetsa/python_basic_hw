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


def frequent_word(text):
    counter = {}
    line = sorted(text.split())
    for word in line:
        if word not in counter:
            counter[word] = line.count(word)
    max_count = max(counter.values())
    for k, v in counter.items():
        if v == max_count:
            return k
    # most_frequent = [k for k, v in counter.items() if v == max_count]
    # print(counter.keys())
    # print(counter.values())


text = input(":")
print(frequent_word(text))


text_1 = "am"
assert frequent_word(text_1) == "am"
text_2 = "am ab asd dfsglsjhdk sdf abc"
assert frequent_word(text_2) == "ab"
text_3 = " sdkfj wefk  wjifljsgiahji k ldfkjefikjew"
assert frequent_word(text_3) == "k"

print("All tests passed successfully!")
