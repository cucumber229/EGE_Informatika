#В текстовом файле записан набор пар натуральных чисел, не превышающих 10 000. Необходимо выбрать из набора некоторые пары так, чтобы первое число в каждой выбранной паре было нечётным, сумма бо́льших чисел во всех выбранных парах была нечётной, а сумма меньших — чётной. Какую наибольшую сумму чисел во всех выбранных парах можно при этом получить?
f = open('numbers')
a = f.read().splitlines()[1:]
mx = 0
mn = 0
min2 = []#макс четное мин нечетное
min1 = []#оба нечетные
min3 = []# макс нечетное мин четное
for i in a:
    x, y = map(int,i.split())
    if x % 2 == 1:
        mx += max(x,y)
        mn += min(x,y)
        if max(x,y) % 2 == 0:
            min2.append(x + y)
        else:
            if min(x,y) % 2 == 0:
                min3.append(x + y)
            else:
                min1.append(x + y)
summa = mx + mn
if mx % 2 == 1 and mn % 2 == 0:
    print(summa)
if mx % 2 == 0 and mn % 2 == 1:
    print(max(summa - min(min1),summa - min(min2)- min(min3)))
if mx % 2 == 1 and mn % 2 == 1:
    print(max(summa - min(min2), summa - min(min1) - min(min3)))
if mx % 2 == 0 and mn % 2 == 0:
    print(max(summa - min(min3), summa - min(min1) - min(min2)))