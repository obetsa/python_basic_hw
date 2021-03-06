"""
    1. Нарисовать границу из * в списке.

    [in]    ['python',
             'django']

    [out]   ['********',
             '*python*',
             '*django*',
             '********']

    [in]    ['abc',
             'def']

    [out]   ['*****',
             '*abc*',
             '*def*',
             '*****']

    Покрыть несколькими тестами.
"""

# Solutions

# 1
def draw_border(input_list: list) -> list:
    c = len(input_list[0]) + 2  # находим количество нужных символов
    return ["*" * c] + [i.center(c, "*") for i in input_list] + ["*" * c]


# 2
def draw_border(input_list: list) -> list:
    border = ["*" * (len(input_list[0]) + 2)]
    for i in input_list:
        border.append("*" + i + "*")

    border.append(border[0])

    return border
