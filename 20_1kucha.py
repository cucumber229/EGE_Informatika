def f(x, p):
    if x >= 52 and p == 3:
        return True
    if x < 52 and p == 3:
        return False
    if x >= 52:
        return False
    if p % 2 == 1:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 2, p + 1)


for i in range(1, 52):
    if f(i, 0):
        print(i)
