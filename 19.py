def f(x, y, p):
    if x + y >= 88 and p == 2:
        return True
    if x + y < 88 and p == 2:
        return False
    else:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 3, y, p + 1) or f(x, y * 3, p + 1)


for i in range(1, 72):
    if f(i, 6, 0):
        print(i)
