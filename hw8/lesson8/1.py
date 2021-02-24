def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


for i in even_range(0, 10):
    print(i)
