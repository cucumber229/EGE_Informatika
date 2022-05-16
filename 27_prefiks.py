a = open('numbers').read().splitlines()
a = a[1:]
a = list(map(int, a))
mins = [0 for i in range(10)]
count = 0
sum = 0
maxi = 0
for i in a:
    sum += i
    if i % 2 == 0:
        count += 1
    ost = count % 10
    if mins[ost] == 0:
        mins[ost] = sum
        maxi = sum
    else:
        maxi = max(maxi, sum - mins[ost])
print(maxi)
