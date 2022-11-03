from turtle import *

color('black', 'red')
m = 100
begin_fill()
left(90)
for i in range(4):
    forward(12*m)
    right(90)
right(30)
end_fill()
color('black', 'green')
begin_fill()
for i in range(2):
    forward(8*m)
    right(60)
    forward(8*m)
    right(120)
end_fill()
canvas = getcanvas()
count = 0
for x in range(-500 * m, 500 * m, m):
    for y in range(-500 * m, 500 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)