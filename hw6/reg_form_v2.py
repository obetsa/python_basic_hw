"""
    Обновите форму регистрации из hw5/reg_form.py таким образом, чтобы:

    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""


def phone():
    phone = input('Введіть номер телефону: ')
    digits = ''
    for char in phone:
        if char.isdigit():
            digits += char

    if len(digits) >= 9:
        phone = '+380' + digits[-9:]
        return phone
    else:
        save_error("Не вірний формат номеру: " + phone)
        print('Не вірний формат')
        return False


def email():
    email = input('Введіть email: ')
    if (len(email) >= 6 and email.count('@') == 1 and
            email[email.rfind('@'):].count('.') >= 1):
        return email
    else:
        save_error("Некорректна електронна адреса: " + email)
        print('Некорректна електронна адреса')
    return


def password():
    upper_case = 0
    lower_case = 0
    number = 0
    symbol = 0
    space = 0
    password = input('Введіть пароль: ')

    for char in password:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char.isdigit():
            number += 1
        elif char.isspace():
            space += 1
            print('Пробіл в паролі')
            return
        else:
            symbol += 1

    if len(password) < 8:
        save_error("Закороткий пароль" + password)
        print('Закороткий пароль')
        return
    elif upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0:
        while (input('Підтвердіть введення паролю: ') != password):
            save_error("Паролі не сходяться. Повторіть спробу: " + password)
            print('Паролі не сходяться. Повторіть спробу')
        else:
            return password
    else:
        save_error("Пароль заслабкий: " + password)
        print('Пароль заслабкий')
        return


def save_user(phone, email, password):
    with open("files/users.txt", "a") as f:
        f.write(f"Phone: {phone} \tEmail: {email} \tPassword: {password}\n")


def save_error(error):
    with open("files/errors.txt", encoding="utf-8", mode="a") as f:
        f.write(f"{error}\n")


def main():
    p = phone()
    while not p:
        p = phone()

    e = email()
    while not e:
        e = email()

    w = password()
    while not w:
        w = password()
    x = '*' * len(w)
    while True:
        save_user(p, e, w)
        print(f'''Вітаємо з успішною реєтрацією!
Ваш номер телефона: {p}
Ваш email: {e}
Ваш пароль: {x}
''')
        break
    return


if __name__ == '__main__':
    main()
