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


def read_book():
    accounts = []
    with open("files/phone_book.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r"\w+(a|A)\b|(m|M)\w+\b", line):
                pname = re.search(r"\w+(a|A)\b|(m|M)\w+\b", line)
                name = pname.group()
                print(name)
                pdigit = re.findall(r"\d+", line)
                digit = "".join(pdigit)
                print(digit)
                accounts.append((digit, name))
    return accounts


def save_book(accounts):
    with open("files/edited_phone_book.txt", "a") as f:
        i = 1
        for account in accounts:
            print(f"{i} {account[0]} - {account[1]}\n")
            f.write(f"{i} {account[0]} - {account[1]}\n")
            i += 1


def main():
    accounts = read_book()
    print(accounts)
    save_book(accounts)


if __name__ == "__main__":
    main()
