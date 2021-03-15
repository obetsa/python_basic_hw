import re
import password_gen
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


def main_menu():
    while(True):
        choice = input(
            ''' \nРеєстрація користувачів:\n
1. Зареєструвати нового користувача
2. Подивитись список користувачів
3. Закрити програму\n\n'''
        )
        if choice == "1":
            reg_user()
        elif choice == "2":
            show()
        elif choice == "3":
            break
        else:
            print("Введіть коректні дані.")


def reg_user():
    user_list = []

    phone = get_phone()
    search_phone_in_file(phone)
    email = get_email()
    password = get_password()

    user_list.append([phone, email, password])
    save_data(phone, email, password)

    print(
        f"\nВітаємо з успішною реєстрацією!"
        f"\nВаш номер телефону: +{phone}"
        f"\nВаш email: {email}"
        f'\nВаш пароль: {"*"*len(password)}'
    )

    if input("Продовжити? (Y/n)") == "n":
        return user_list
    return reg_user()

    user_data = user_list[0]
    print("\n" + user_data[0], user_data[1], user_data[2])


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
    phone = input("Введіть номер телефону: ")
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
                print("Такий номер уже існує! Зареєструйте іншого користувача")
                return main_menu()
    return list_of_results


def get_email():
    email = input("Введите email: ")
    if len(email) < 6 or email.count("@") != 1 or email.startswith("@"):
        print("Невірний формат. Повторіть введення даних.")
        return get_email()
    return email


def get_password():
    password = input("Введите пароль: ")
    if len(password) < 8 or re.findall(r"\s", password):
        print("Пароль занадто слабкий. Придумайте більш надійніший пароль.")
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
        print("Пароль занадто слабкий. Придумайте більш надійніший пароль.")
        return get_password()

    if input("Повторіть введення паролю: ") != password:
        print("Паролі не співпадають.")
        return get_password()
    return password


def show():
    with open(BASE_DIR / "users.txt", "r") as f:
        f.seek(0)
        data = f.readlines()
        a = len(data)
        if a > 1:
            b = "{}".format(a)
            print('В базі ' + b + ' користувачів')
        else:
            b = "{}".format(a)
            print('В базі ' + b + ' користувач')

        choice = input(
            "Відобразити всіх користувачів? (Y/n)\n"
        )
        if choice == "y":
            show_phone()
            user_statistic()
        elif choice == "n":
            main_menu()
        else:
            print("Введіть коректні дані, виберіть: 'y' або 'n'")
            return show()


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


def user_data(numb):
    data = read_data()
    print(data[numb])
    return menu_user()


def user_statistic():
    numb = int(input(
            "\nВведіть номер по списку,"
            "для перегладу деталей користувача: "))
    numb -= 1
    with open(BASE_DIR / "users.txt", "r") as f:
        f.seek(0)
        data = f.readlines()
        print('\n' + data[numb])

    return menu_user(numb)


def menu_user(numb):
    choice = input(
            "\n1. Змінити пароль\n"
            "2. Видалити користувача\n"
            "3. Повернутись в головне меню\n"
        )
    if choice == "1":
        generate_pass(numb)
    elif choice == "2":
        delete_user(numb)
    elif choice == "3":
        main_menu()
    else:
        print("Введіть коректні дані.")


def generate_pass(numb):
    data = read_data()
    d = data[numb]
    d = d.split(' ')
    d.pop()
    light_p = password_gen.main()
    print("Пароль змінено на: " + light_p)
    d.append(light_p)
    data[numb] = ' '.join(d) + '\n'
    with open(BASE_DIR / "users.txt", "w") as f:
        for lines in data:
            f.write('%s' % lines)
    return


def delete_user(numb):
    data = read_data()
    d = data[numb]
    with open(BASE_DIR / "users.txt", "w") as f:
        for line in data:
            if line != d:
                f.write(line)


def main():
    main_menu()


if __name__ == "__main__":
    main()
