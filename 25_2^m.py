count = []
for m in range(2, 30, 2):
    for n in range(1, 30, 2):
        N = (2 ** m) * (3 ** n)
        if N in range(200000000, 400000000):
            count.append(N)
count.sort()
print(*count)