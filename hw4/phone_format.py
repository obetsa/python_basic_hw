"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.
    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""

phone = input('Enter phone number: ')
number = ''.join(char for char in phone if char.isdigit())
if number.rfind('8', 0, 5) >= 1:
    number = '3' + number[number.rfind('8', 0, 5) :]
    if len(number) == 12:
        print(number)
    else:
        print("Недостатньо цифр в номері, повторіть")
elif number[:1] == '8':
    number = '3' + number
    if len(number) == 12:
        print(number)
    else:
        print("Недостатньо цифр в номері, повторіть")
# elif number[:2] == '38':
#     if len(number) == 12:
#         print(number)
#     else:
#         print("Недостатньо цифр в номері, повторіть")
else:
    number = '38' + number
    if len(number) == 12:
        print(number)
    else:
        print("Недостатньо цифр в номері, повторіть")

