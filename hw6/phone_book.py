"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).

    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""
import re


def phone():
    with open("files/phone_book.txt", "r") as f:
        lines = f.readlines()
        matches = []
        for line in lines:
            if re.search(r"w+(a|A)\b|(m|M)\w+\b", line):
                matches += line
        for match in matches:
            name = (re.findall(r'\w+', match))
            # number = re.search(r'\d+')
            print(name)

# re.match(r"([m|M])\w+\b", line)    
# or re.match(r"([aA])\w+", line):
# re.findall(r"[a-zA-Z]+", string)     


# def written():
#     with open("files/phone_book.txt", "w") as f:
            




def main():
    phone()
#     name = get_name()
#     surname = input("+Enter your surname: ")
#     age = input("Enter your age: ")

#     save_info(name, surname, age)

if __name__ == "__main__":
    main()
