while True:  # объявляем бесконечный цикл
    year = int(input("year: "))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(366)
    else:
        print(365)

    if input("Continue? (Y/n) ") == "n":  # в конце цикла условие
        break