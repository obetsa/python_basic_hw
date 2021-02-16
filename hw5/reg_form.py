"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())_
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
    Программа выводит сообщение:
    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)
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
        print('Не вірний формат')
        return False


def email():
    email = input('Введіть email: ')
    if (len(email) >= 6 and email.count('@') == 1 and
            email[email.rfind('@'):].count('.') >= 1):
        return email
    else:
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
        print('Закороткий пароль')
        return
    elif upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0:
        while (input('Підтвердіть введення паролю: ') != password):
            print('Паролі не сходяться. Повторіть спробу')
        else:
            return password
    else:
        print('Пароль заслабкий')
        return


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
        print(f'''Вітаємо з успішною реєтрацією!
Ваш номер телефона: {p}
Ваш email: {e}
Ваш пароль: {x}
''')
        break
    return


if __name__ == '__main__':
    main()
