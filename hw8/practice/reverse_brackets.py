"""
    Реверс подстроки в ()

    Таким образом, чтоб:
    [in]    "(bar)"
    [out]   "rab"

    [in]    "foo(bar)baz"
    [out]   "foorabbaz"

    [in]    "foo(bar)baz(blim)"
    [out]   "foorabbazmilb"

    [in]    "foo(bar(baz))blim"
    [out]   "foobazrabblim"
    так как "foo(bar(baz))blim" -> "foo(barzab)blim" -> "foobazrabblim"

    Данные примеры можете использовать для написания тестов.
"""


def reverse_brackets(s: str) -> str:
    n = len(s)
    x = " "
    for i in range(n - 1, -1, -1):
        x += s[i]
    return x
    print(x)


s = input("(bar)")
reverse_brackets(s)
