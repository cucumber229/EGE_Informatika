m = 4000000
counter = 0
listA = []
listB = []
prices = []
a = open('17.txt').read().splitlines()
for i in a:
    price, count, x = map(str,i.split())
    price, count = int(price),int(count)
    if x == 'A':
        s = [price, count, x]
        listA.append(s)
    if x == 'B':
        s = [price, count, x]
        listB.append(s)
listB.sort()
for i in listA:
    m -= i[0] * i[1]
for i in range(len(listB)):
    m -= listB[i][0] * listB[i][1]
    counter += listB[i][1]
    prices.append(listB[i][0])
    if m - listB[i][0] in prices:
        print(m - listB[i + 1][0])
    if m < listB[i][0] * listB[i][1]:
        break
print(counter + 1)