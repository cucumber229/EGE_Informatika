def f(x, p):
    if x >= 65 and p == 2:
        return True
    if x < 65 and p == 2:
        return False
    else:
        return f(x + 1, p + 1)  or f(x * 2, p + 1)


for i in range(1, 65):
    if f(i, 0):
        print(i)
