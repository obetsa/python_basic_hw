"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, которые не меньше размера его ноги.

    Напишите функцию, которая принимает список доступных размеров коньков и
    список размеров ног желающих.

    И возвращает наибольшее количество людей,
    которые смогут покататься одновременно.


    Например:
    [in]
    [39, 38, 41, 37] (доступные размеры)
    [40, 39, 41] (размеры ног желающих)

    [out]
    2

    [37, 38, 39, 40] , [37, 37, 40, 40] -> 3
    [37, 38, 39, 40] , [42] -> 0
    [37, 38, 39] , [37, 37, 37, 37] -> 3

    Напишите несколько тестов
"""

# Solutions

# 1
def skates(available_sizes, foot_sizes):
    res_list = []
    for i in available_sizes:
        for j in foot_sizes:
            if j <= i and len(res_list) < len(available_sizes):
                res_list.append(i)
                foot_sizes.remove(j)
    return len(res_list)


list_available = [37, 38, 39, 40]
list_foot = [37, 37, 40, 40]
assert skates(list_available, list_foot) == 3

list_available = [39, 38, 41, 37]
list_foot = [40, 39, 41]
assert skates(list_available, list_foot) == 2

print("All tests passed successfully")


# 2
def skates(available_sizes, foot_sizes):
    available = sorted(list(map(int, available_sizes.split())))
    desired = sorted(list(map(int, foot_sizes.split())))
    count = 0
    while True:
        try:
            available = list(filter(lambda x: x >= min(desired), available))
            available.pop(0)
            desired.pop(0)
            count += 1
        except IndexError:
            break
    return count


list_available = "37 38 39 40"
list_foot = "37 37 40 40"
assert skates(list_available, list_foot) == 3

list_available = "39 38 41 37"
list_foot = "40 39 41"
assert skates(list_available, list_foot) == 2

print("All tests passed successfully")
