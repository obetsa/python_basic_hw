"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:

    1. Все сгенерированные пароли записывались в файл.
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".

    *3. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.

    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается

"""


import string
import random


def gen_password(pattern, size):
    password = "".join(random.sample(pattern, size))
    return password


def l_password():
    size = 8
    pattern = (string.ascii_lowercase)
    password = gen_password(pattern, size)
    return password


def m_password():
    size = 8
    lowercase = (string.ascii_lowercase)
    uppercase = (string.ascii_uppercase)
    number = (string.digits)
    pattern = uppercase + lowercase + number
    password = gen_password(pattern, size)
    return password


def s_password():
    size = random.randint(8, 16)
    password = ''
    lowercase = (string.ascii_lowercase)
    uppercase = (string.ascii_uppercase)
    number = (string.digits)
    symbols = (string.punctuation)
    strong = uppercase + lowercase + number + symbols
    for i in range(size):
        password += random.choice(strong)
    counter_d = counter_u = counter_l = counter_s = 0
    for char in password:
        if char.isdigit():
            counter_d += 1
        elif char.isupper():
            counter_u += 1
        elif char.islower():
            counter_l += 1
        elif not char.isspace():
            counter_s += 1
    if counter_d > 0 and counter_u > 0 and counter_l > 0 and counter_s > 0:
        return password
    return s_password()


def user_password():
    sumbols = input('Введіть символи з яких буде генеруватися пароль: ')
    size_p = int(input('Введіть довжину пароля: '))
    if size_p <= 8:
        print('Пароль не надійний')
    # password = input("Enter pass:")
    password = gen_password(sumbols, size_p)
    return password


def insecure_password(password):
    with open("hw6/files/password.txt", "r") as f:
        file = f.read()
    if file.find(password) > 0:
        print("Insecure password")
        return True
    else:
        return False


def save_pass(password):
    with open("hw6/files/password.txt", "a") as f:
        f.write(f"Password: {password}\n")


def main():
    print('''Виберіть пароль:
1 - легкий
2 - середній
3 - тяжкий
4 - пароль користувача''')
    choise_pass = int(input(''))
    if choise_pass == 1:
        password = l_password()
        while insecure_password(password):
            password = l_password()
    elif choise_pass == 2:
        password = m_password()
        while insecure_password(password):
            password = m_password()
    elif choise_pass == 3:
        password = s_password()
        while insecure_password(password):
            password = s_password()
    elif choise_pass == 4:
        password = user_password()
        while insecure_password(password):
            password = user_password()
    else:
        print('Невірні дані, спробуйти ще раз')
    print(password)
    save_pass(password)
    return


if __name__ == '__main__':
    main()
