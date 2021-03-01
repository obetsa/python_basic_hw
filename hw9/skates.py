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


# def skates(available_sizes, foot_sizes):
#     pass

skates = sorted(list(map(int,input().split()))) # получаем сортированные списки чтоб минимальные были первыми
visitors = sorted(list(map(int,input().split())))
res = 0
while True: # пока не закончатся коньки или посетители
    try:
        skates = list(filter(lambda x : x>= min(visitors), skates)) # отбрасываем меньше мин размера
        skates.pop(0) # отдаем коньки (удаляем) первые из списка которые точно не меньше мин размера
        # первого в списке посетителя
        visitors.pop(0) # удаляем посетителя из списка
        res += 1 # считаем
        # если еще есть коньки или посетители начинаем заново с отбрасываем меньше мин размера
    except:
        break
print(res)
