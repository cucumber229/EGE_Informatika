def binary(elem,arr,start,end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == elem:
        return True
    if elem < arr[mid]:
        return binary(elem, arr, start, mid - 1)
    else:
        return binary(elem, arr, mid + 1, end)
a = open('17.txt').read().splitlines()[1:]
a = list(map(int,a))
a.sort()
count = 0
max = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] % 2 != a[j] % 2:
            sum = a[i] + a[j]
            if binary(sum, a, 0, len(a) - 1):
                count += 1
                if sum > max:
                    max = sum
print(count,max)