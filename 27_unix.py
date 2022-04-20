a = open('17.txt').read().splitlines()[1:]
start_time = 1634515200
end_time = 1634515200 + 604800
count = 0
time = [0 for i in range(1, 604801)]
for i in a:
    start, end = map(int, i.split())
    if (start < start_time) and ((end > start_time) or (end == 0)):
        count += 1
    if (start >= start_time) and (start <= end_time):
        time[start - start_time] = time[start - start_time] + 1
    if (end >= start_time) and (end <= end_time):
        time[end - start_time] = time[end - start_time] - 1
sum_time = 0
max = 0
for i in range(1, 604800):
    count += time[i]
    if count > max:
        max = count
        sum_time = 0
    if count == max:
        sum_time += 1

print(max, sum_time)
