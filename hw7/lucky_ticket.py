"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    x = int(len(ticket_num) // 2)
    a = ticket_num[:x]
    b = ticket_num[x:]
    if sum(map(int, a)) == sum(map(int, b)):
        print(True)
    else:
        print(False)


ticket_num = input(": ")
is_lucky(ticket_num)


# assert is_lucky(1230) is True
# assert is_lucky(239017) is False
# assert is_lucky(134008) is True
# assert is_lucky(15) is False
# assert is_lucky(2020) is True
# assert is_lucky(199999) is False
# assert is_lucky(77) is True
# assert is_lucky(479974) is True

# print("All tests passed successfully!")
