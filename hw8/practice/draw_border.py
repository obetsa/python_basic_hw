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


def draw_border(input_list: list) -> list:
    x = '*' * len(input_list)
    print(x)
    input_list.insert(0, 'pre')
    print(input_list)


input_list = ('python', 'django')
draw_border(input_list)
