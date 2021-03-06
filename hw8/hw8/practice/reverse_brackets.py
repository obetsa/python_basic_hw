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
import re

# Solutions

# 1
def reverse_brackets(s: str) -> str:
    end = s.find(")")
    start = s.rfind("(", 0, end)
    if end == -1:
        return s
    return reverse_brackets(
        s[:start] + s[start + 1 : end][::-1] + s[end + 1 :]
    )


# 2
def reverse_brackets(s: str) -> str:
    search_result = re.search(r"\(\w*\)", s)
    if search_result:
        before = search_result.group()
        after = before.replace("(", "").replace(")", "")[::-1]
        return reverse_brackets(s.replace(before, after))
    return s


# 3
def reverse_brackets(s: str) -> str:
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverse_brackets(
                s[:start] + s[start + 1 : end][::-1] + s[end + 1 :]
            )
    return s
