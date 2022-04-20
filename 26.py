import collections
a = open('В ТЗ вставить вместе с 26 заданием с файла сверху.txt').read().splitlines()[1:]
count = []
for i in a:
    x, y = map(int,i.split())
    if y % 2 == 0:
        count.append(x)
print(collections.Counter(count))