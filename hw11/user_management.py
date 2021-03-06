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
            - номер телефона - уникальный (нельзя зарегистрировать двух пользователей с одинаковым номером телефона)
            - после успешной регистрации выводятся данные о пользователе и попадаем в Главное меню
            - данные о пользователе сохраняются:
                + в переменной
                + для хранения пользователей можно использовать любую структуру данных
                * использовать список словарей либо список объектов класса
                ** сохранять данные в файл (при перезапуске программы данные не теряются)

        При выборе пункта 2.
            - выводится количество зарегистрированных пользователей и
                задается вопрос: "Отобразить всех пользователей? (да/нет)"

                нет - попадаем в Главное меню
                да - переходим к следующему пункту

            - на экран выводится пронумерованный список пользователей (только номера телефонов)
            ** при выборе порядкового номера пользователя показывается детальная информация о пользователе
            ** после детальной информации выбор:
                1. Сбросить пароль
                    - пользователю генерируется новый случайный пароль
                    - отображается на экране
                    - возвращаемся в Главное меню
                2. Удалить пользователя
                    - * можно добавить подтверждение ("Вы действительно хотите удалить пользователя +380501234567? (да, нет)")
                    - возвращаемся в Главное меню

"""


import re
from pathlib import Path


def main():
    choice = input(
        "1. Зарегистрировать нового пользователя\n"
        "2. Просмотреть список пользователей\n"
    )
    if choice == "1":
        reg()
    elif choice == "2":
        

    print()




BASE_DIR = Path(__file__).resolve().parent


def main():
    user_list = []

    while True:
        phone = get_phone()
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

    print(user_list)
    user_data = user_list[0]
    print(user_data[0], user_data[1], user_data[2])

    with open(BASE_DIR / "users.txt", "a") as f:
        for phone, email, password in user_list:
            print(f"{phone} {email} {password}", file=f)


def save_data(phone, email, password):
    with open(BASE_DIR / "users.txt", "a") as f:
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


if __name__ == "__main__":
    main()