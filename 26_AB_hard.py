a = open('17.txt').read().splitlines()[1:]
price = 982000
count = []
countA = []
countB = []
for i in a:
    x, y = i.split()
    count.append([int(x),y])
count.sort()
sum = 0
c = 0
ost_price = 0
for i in count:
    price -= i[0]
    if price > 0:
        sum += i[0]
        ost_price = price
        if i[1] == "B":
            c += 1
        if i[1] == "A":
            countA.append(i)
    else:
        if i[1] == 'B':
            countB.append(i)
countA.sort(reverse=True)
for x in countA:
    if ost_price + x[0] - countB[0][0] > 0:
        c += 1
        ost_price += x[0] - countB[0][0]
        countB = countB[1:]
print(c,ost_price)
