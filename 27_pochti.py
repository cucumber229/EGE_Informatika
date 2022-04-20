f = open('17.txt')
a = f.read().splitlines()
a = a[1:]
s = 0
count_chet = 0
count_nechet = 0
max_nechet = []
max_chet = []
for i in a:
    x, y = map(int,i.split())
    s += min(x, y)
    if min(x,y) % 2 == 0:
        count_chet += 1
    if min(x,y) % 2 == 1:
        count_nechet += 1
    div = abs(x - y)
    if div % 2 == 1:
        max_nechet.append(div)
    if div % 2 == 0:
        max_chet.append(div)
max_chet.sort()
max_nechet.sort()
div1_nechet = max_nechet[0]
div2_nechet = max_nechet[1]
div1_chet = max_chet[0]
div2_chet = max_chet[1]
if count_chet > count_nechet:
    if s % 2 == 1 and div1_nechet > div1_chet + div2_chet:
        print(s + div1_chet + div2_chet)
    elif s % 2 == 1 and div1_nechet < div1_chet + div2_chet:
        print(s + div1_nechet)
    if s % 2 == 0:
        print(s)
else:
    if s % 2 == 0 and div1_chet > div1_nechet + div2_nechet:
        print(s + div1_nechet + div2_nechet)
    elif s % 2 == 0 and div1_chet < div1_nechet + div2_nechet:
        print(s + div1_chet)
    if s % 2 == 1:
        print(s)