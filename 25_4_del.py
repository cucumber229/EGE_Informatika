def f(n):
    count = []
    for x in range(1, n + 1):
        if n % x == 0:
            count.append(x)
    if len(count) == 4:
        return count


for n in range(185311, 185330 + 1):
    if f(n):
        print(*f(n))