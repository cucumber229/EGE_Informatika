def f(x, p, ban):
    if x >= 34 and p == 3:
        return True
    if x < 34 and p == 3:
        return False
    if x >= 34:
        return False
    if p % 2 == 0:
        if ban == 1:
            return f(x + 2, p + 1, 2) or f(x * 2, p + 1, 3)
        elif ban == 2:
            return f(x + 1, p + 1, 1) or f(x * 2, p + 1, 3)
        elif ban == 3:
            return f(x + 1, p + 1, 1) or f(x + 2, p + 1, 2)
        elif ban is None:
            return f(x + 1, p + 1, 1) or f(x + 2, p + 1, 2) or f(x * 2, p + 1, 3)
    else:
        if ban == 1:
            return f(x + 2, p + 1, 2) and f(x * 2, p + 1, 3)
        elif ban == 2:
            return f(x + 1, p + 1, 1) and f(x * 2, p + 1, 3)
        elif ban == 3:
            return f(x + 1, p + 1, 1) and f(x + 2, p + 1, 2)


for i in range(1, 34):
    if f(i, 0, None):
        print(i)
