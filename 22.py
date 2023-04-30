a = open('test').read()
a = a.replace(';', ' ').splitlines()
ans = [0] * len(a)
for i in a:
    i = i.split()
    idd = int(i[0])
    time = int(i[1])
    sub = list(map(int, i[2:]))
    if sub[0] == 0:
        ans[idd - 1] = time
    else:
        ans[idd - 1] = max(ans[j - 1] for j in sub) + time
print(max(ans))
