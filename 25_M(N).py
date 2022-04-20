def f(n):
    count = []
    for x in reversed(range(2, n)):
        if n % x == 0:
            count.append(x)
    if len(count) == 2:
        return sum(count)
    else:
        return 0


for n in range(11000001, 110000010):
    if 0 < f(n) < 10000:
        print(f(n))
