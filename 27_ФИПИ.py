a = open('numbers').read().splitlines()
a = a[1:]
a = list(map(int,a))
sums = []
n = len(a)
for j in range(n):
    print(j)
    sum = 0
    for i in range(n):
        s = min(abs(i - j),n - abs(i - j))
        sum += a[i] * s * 3
    sums.append(sum)
print(min(sums))