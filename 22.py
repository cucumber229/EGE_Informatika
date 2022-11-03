a = open('test').read().splitlines()
arr = []
for i in a:
    id, time, dep = i.split()
    id = int(id)
    time = int(time)
    dep = list(map(int, dep.split(';')))
    if dep[0] == 0:
        arr.append(time)
    else:
        if len(dep) > 1:
            mx = max([arr[dep[i] - 1] for i in range(len(dep))])
            arr.append(time + mx)
        else:
            arr.append(time + arr[dep[0] - 1])
print(max(arr))
