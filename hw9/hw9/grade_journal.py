"""
    Пользователь вводит количество студентов N.
    После чего вводит N строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""


def main():
    number = input("Enter the number of students: ")
    if number.isdigit():
        number = int(number)
    else:
        print("Not a number.")
        return main()

    student_list = []
    for _ in range(number):
        surname, grade = input("Enter student surname and grade: ").split()
        if not grade.isdigit():
            print("invalid grade, this student ignored")
            continue

        # для хранения данных можно использовать кортеж либо словарь
        student_list.append((surname, int(grade)))
        # student_list.append({"surname": surname, "grade": grade})

    student_list.sort(key=lambda s: s[1], reverse=True)
    # student_list.sort(key=lambda s: s["grade"], reverse=True)
    for index, student in enumerate(student_list):
        print(f"{index + 1}. {student[0]}")
        # print(f"{index + 1}. {student['surname']}")


if __name__ == "__main__":
    main()
