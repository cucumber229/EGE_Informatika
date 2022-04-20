f = open('17.txt')
a = f.read().splitlines()
count = 0
min_raz_1 = 1000000
min_raz_2 = 1000000
min_raz_3 = 1000000
min_raz_4 = 1000000

for i in a:
    x, y = map(int,i.split())
    count += min(x,y)
    raz = abs(x - y)
    if raz % 5 == 1 and raz < min_raz_1:
        min_raz_1 = raz
    if raz % 5 == 2 and raz < min_raz_2:
        min_raz_2 = raz
    if raz % 5 == 3 and raz < min_raz_3:
        min_raz_3 = raz
    if raz % 5 == 4 and raz < min_raz_4:
        min_raz_4 = raz
if count % 5 == 0:
    print(count)
if count % 5 == 1:
    print(count + min_raz_4)
if count % 5 == 2:
    print(count + min_raz_3)
if count % 5 == 3:
    print(count + min_raz_2)
if count % 5 == 4:
    print(count + min_raz_1)