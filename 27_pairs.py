#Набор данных состоит из пар натуральных чисел. Необходимо выбрать из набора некоторые пары так, чтобы второе число в каждой выбранной паре было нечётным, сумма бо́льших чисел во всех выбранных парах была чётной, а сумма меньших – нечётной. Какую наибольшую сумму чисел во всех выбранных парах можно при этом получить?
a = open('numbers').read().splitlines()
mx = 0
mn = 0
x0 = []
x1 = []
for i in a:
    x, y = map(int,i.split())
    if y % 2 != 0:
        mx += max(x,y)
        mn += min(x,y)
        if x % 2 == 0:
            x0.append(x + y)
        else:
            x1.append(x + y)
x0.sort()
x1.sort()
if mx % 2 == 0 and mn % 2 == 0:
    print(mx + mn - min(x0))
if mx % 2 == 1 and mn % 2 == 1:
    print(mx + mn - min(x0) - min(x1))
if mx % 2 == 1 and mn % 2 == 0:
    print(mx + mn - min(x1))
if mx % 2 == 0 and mn % 2 == 1:
    print(max(mx + mn - x1[0] - x1[1]),(mx + mn - x0[0] - x0[1]))
