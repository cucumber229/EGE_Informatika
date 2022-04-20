def f(n):
    count = []
    for x in reversed(range(2, n)):
        if n % x == 0:
            count.append(x)
    if len(count) == 0:
        return 0
    else:
        return count[0] + count[-1]


for n in range(700000, 7000000):
    if f(n) % 10 == 8:
        print(n, f(n))