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
from pathlib import Path

FILES_DIR = Path(__file__).resolve().parent / "files"


def main():
    with open(FILES_DIR / "phone_book.txt") as f_in:
        with open(FILES_DIR / "edited_phone_book.txt", "a") as f_out:
            num = 1
            for line in f_in.readlines():
                name = "".join(char for char in line if char.isalpha()).lower()

                if name.startswith("m") or name.endswith("a"):
                    phone = "".join(char for char in line if char.isdigit())
                    phone = "+380" + phone[-9:]
                    print(f"{num}. {phone} - {name.title()}", file=f_out)
                    num += 1


if __name__ == "__main__":
    main()

# import re

# with open("hw6/files/phone_book.txt") as f:
#     idx = 1
#     for line in f.readlines():
#         # получить имя
#         # 1 вариант в две строкиy
#         # name_phone = re.sub(r"\W", "", line)
#         # name = re.sub(r"\d", "", name_phone).lower()

#         # 2 вариант в одну строку
#         name = re.sub(r"(\W|\d)", "", line).lower()

#         if name[0] == "m" or name[-1] == "a":
#             phone = "+380" + re.sub(r"\D", "", line)[-9:]
#             with open("hw6/files/edited_phone_book.txt", "a") as f:
#                 print(f"{idx}. {phone} - {name.title()}", file=f)
#                 idx += 1
