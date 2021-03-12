"""
    User management.

    * - рекомендации
    ** - более сложные условия для высшего балла

        Основные возможности программы:
            - регистрация пользователей
            - просмотр учетных записей
            - хранение базы пользователей в течении сеанса
            ** хранение базы пользователей в файле
            ** сброс пароля пользователей
            ** удаление пользователей

        При запуске программы попадаем в "Главное меню":
            1. Зарегистрировать нового пользователя
            2. Просмотреть список пользователей

        При выборе пункта 1.
            - форма регистрации, аналогичная из hw5/reg_form.py, а именно:
                + ввод номера телефона
                + ввод email адреса
                + ввод и подтверждение пароля
            - номер телефона - уникальный (нельзя зарегистрировать двух
            пользователей с одинаковым номером телефона)
            - после успешной регистрации выводятся данные о пользователе
            и попадаем в Главное меню
            - данные о пользователе сохраняются:
                + в переменной
                + для хранения пользователей можно использовать любую
                 структуру данных
                * использовать список словарей либо список объектов класса
                ** сохранять данные в файл (при перезапуске программы данные
                 не теряются)

        При выборе пункта 2.
            - выводится количество зарегистрированных пользователей и
                задается вопрос: "Отобразить всех пользователей? (да/нет)"

                нет - попадаем в Главное меню
                да - переходим к следующему пункту

            - на экран выводится пронумерованный список пользователей
             (только номера телефонов)
            ** при выборе порядкового номера пользователя показывается
             детальная информация о пользователе
            ** после детальной информации выбор:
                1. Сбросить пароль
                    - пользователю генерируется новый случайный пароль
                    - отображается на экране
                    - возвращаемся в Главное меню
                2. Удалить пользователя
                    - * можно добавить подтверждение ("Вы действительно хотите
                     удалить пользователя +380501234567? (да, нет)")
                    - возвращаемся в Главное меню

"""


import re
# import random
# import string
import password_gen
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


def main_menu():
    while(True):
        choice = input(
            "1. Зарегистрировать нового пользователя\n"
            "2. Просмотреть список пользователей\n"
            "3. Close program\n"
        )
        if choice == "1":
            reg_user()
        elif choice == "2":
            show()
        elif choice == "3":
            break
        else:
            print("Enter correct num!!")

        # if input("Continue? (Y/n)") == "n":
        #         break


def reg_user():
    user_list = []

    while True:
        phone = get_phone()
        search_phone_in_file(phone)
        email = get_email()
        password = get_password()

        user_list.append([phone, email, password])
        save_data(phone, email, password)

        print(
            f"\nПоздравляем с успешной регистрацией!"
            f"\nВаш номер телефона: +{phone}"
            f"\nВаш email: {email}"
            f'\nВаш пароль: {"*"*len(password)}'
        )

        if input("Continue? (Y/n)") == "n":
            break
        main_menu()

    print(user_list)
    user_data = user_list[0]
    print(user_data[0], user_data[1], user_data[2])

    # with open(BASE_DIR / "users.txt", "a") as f:
    #     for phone, email, password in user_list:
    #         print(f"{phone} {email} {password}", file=f)


def save_data(phone, email, password):
    with open(BASE_DIR / "users.txt", "a") as f:
        f.seek(0)
        print(f"{phone} {email} {password}", file=f)


def formatted_phone(phone):
    phone = "".join(s for s in phone if s.isdigit())
    return "380" + phone[-9:]


def phone_valid(phone):
    if len(phone) == 12 and phone.isdigit():
        return True
    return False


def get_phone():
    phone = input("Enter phone number:")
    phone = formatted_phone(phone)

    if phone_valid(phone) is True:
        return phone
    return get_phone()


def search_phone_in_file(phone):
    line_number = 0
    list_of_results = []
    with open(BASE_DIR / "users.txt", 'r') as f:
        for line in f:
            line_number += 1
            if phone in line:
                print("number exists? enter another")
                return get_phone()
        # return phone
            # return get_phone()
                # list_of_results.append((line_number, line.rstrip()))
    return list_of_results


def get_email():
    email = input("Введите email: ")
    if len(email) < 6 or email.count("@") != 1 or email.startswith("@"):
        print("Неверный формат. Повторите ввод.")
        return get_email()
    return email


def get_password():
    password = input("Введите пароль: ")
    if len(password) < 8 or re.findall(r"\s", password):
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        return get_password()

    u_counter = l_counter = d_counter = s_counter = 0
    for i in password:
        if i.isupper():
            u_counter += 1
        elif i.islower():
            l_counter += 1
        elif i.isdigit():
            d_counter += 1
        else:
            s_counter += 1

    if min(u_counter, l_counter, d_counter, s_counter) == 0:
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        return get_password()

    if input("Повторите пароль: ") != password:
        print("Пароли не совпадают.")
        return get_password()
    return password


def show():
    with open(BASE_DIR / "users.txt", "r") as f:
        f.seek(0)
        data = f.readlines()
        print(len(data))

        choice = input(
            "Отобразить всех пользователей? (y/n)\n"
        )
        if choice == "y":
            show_phone()
            menu_user()
        elif choice == "n":
            main_menu()
        else:
            print("Enter correct data!!!")


def show_phone():
    with open(BASE_DIR / "users.txt", "r") as f:
        data = f.readlines()
        f.seek(0)
        num = 1
        for line in data:
            u_phone = "".join(char for char in line if char.isdigit())
            u_phone = u_phone[:12]
            print(f"{num}. {u_phone}")
            num += 1
    return


def read_data():
    with open(BASE_DIR / "users.txt", "r") as f:
        data = f.readlines()
    return data


def user_data(uid):
    data = read_data()
    print(data[uid])
    return menu_user()


def menu_user():
    choice = input(
            "\n1. Сбросить пароль\n"
            "2. Удалить пользователя\n"
        )
    if choice == "1":
        uid = int(input("Please enter ID number: "))
        uid -= 1
        generate_pass(uid)
    elif choice == "2":
        uid = int(input("Please enter ID number: "))
        uid -= 1
        delete_user(uid)
    else:
        print("Enter correct data!!!")


def generate_pass(uid):
    data = read_data()
    d = data[uid]
    d = d.split(' ')
    # print(d)
    d.pop()
    # print(d)
    # size = 8
    # lowercase = (string.ascii_lowercase)
    # light_p = "".join(random.sample(lowercase, size))
    light_p = password_gen.main()
    print(light_p)
    d.append(light_p)
    # print(d)
    data[uid] = ' '.join(d) + '\n'
    with open(BASE_DIR / "users.txt", "w") as f:
        for lines in data:
            # f.seek(0)
            f.write('%s' % lines)
    return


def delete_user(uid):
    data = read_data()
    d = data[uid]
    with open(BASE_DIR / "users.txt", "w") as f:
        for line in data:
            if line != d:
                f.write(line)


def main():
    main_menu()


if __name__ == "__main__":
    main()


# https://code-projects.org/bakery-shop-chatbot-in-python-with-source-code/
# https://code-projects.org/student-management-system-in-python-with-source-code/
# https://code-projects.org/user-management-system-in-python-with-source-code/
# https://code-projects.org/c/languages/project/pythonprojects/page/8/
# https://www.google.com/search?safe=strict&sxsrf=ALeKk01MtC_CTVBJJG2evcWEYyO5vZbBUQ%3A1615155396699&ei=xFBFYIumKvGMrgTpraD4Dw&q=python+casino&oq=python+casino&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEMsBMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMggIABAWEAoQHjoHCCMQsAMQJzoHCAAQRxCwA1DKuAFYyrgBYK-7AWgBcAJ4AIABkAGIAfEBkgEDMS4xmAEAoAEBqgEHZ3dzLXdpesgBCcABAQ&sclient=gws-wiz&ved=0ahUKEwiLmLXdmp_vAhVxhosKHekWCP8Q4dUDCA4&uact=5
