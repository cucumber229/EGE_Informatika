a = open('numbers').read().splitlines()
a = a[1:]
s = 0
ch_0 = 0
ch_1 = 0
min_dif_1 = []
min_dif_0 = []
for i in a:
    x, y = map(int,i.split())
    s += max(x,y)
    if max(x,y) % 2 == 0:
        ch_0 += 1
    else:
        ch_1 += 1
    if abs(x - y) % 2 != 0:
        min_dif_1.append(abs(x - y))
    if abs(x - y) % 2 == 0:
        min_dif_0.append(abs(x - y))
min_dif_0.sort()
min_dif_1.sort()
print(s,ch_1,ch_0)
if s % 2 == 0 and ch_1 < ch_0:
    print(s)
if s % 2 == 1 and ch_1 > ch_0:
    print(s)
else:
    print(max(s - min_dif_1[0] - min_dif_1[1], s - min_dif_0[0]))