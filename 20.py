def f(x, y, p):
    if x + y >= 88 and p == 3:
        return True
    if x + y < 88 and p == 3:
        return False
    if x + y >= 88:
        return False
    if p % 2 == 1:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 3, y, p + 1) and f(x, y * 3, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 3, y, p + 1) or f(x, y * 3, p + 1)


for i in range(1, 72):
    if f(6, i, 0):
        print(i)
