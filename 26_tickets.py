f = open('17.txt')
a = f.read().splitlines()[1:]
count = []
for i in a:
    x, y = map(int, i.split())
    s = [x, y]
    count.append(s)
count.sort()
for i in range(len(count) - 1):
    if count[i][0] == count[i + 1][0] and count[i][1] + 3 == count[i + 1][1]:
        print(count[i][0], count[i][1] + 1)