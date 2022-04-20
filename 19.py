from math import ceil
def f(x, y, p):
    if x + y <= 40 and p == 2:
        return True
    if x + y > 40 and p == 2:
        return False
    else:
        return f(x - 1, y, p + 1) or f(x, y - 1, p + 1) or f(ceil(x / 2), y, p + 1) or f(x, ceil(y / 2), p + 1)


for i in range(20, 1000):
    if f(20, i, 0):
        print(i)
