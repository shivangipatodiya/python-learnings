import turtle as t
import random
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
              (174, 94, 97), (176, 192, 209)]
t.colormode(255)
t.hideturtle()
t.penup()
t.back(160)
t.pendown()
t.speed('fastest')


def change_line(direction):
    t.penup()
    t.back(20)
    if direction == 'right':
        t.right(90)
        t.forward(20)
        t.right(90)
    else:
        t.left(90)
        t.forward(20)
        t.left(90)


direction = 'right'


def put_dots_on_line():
    for position in range(10):
        t.dot(12, random.choice(color_list))
        t.penup()
        t.forward(20)
        t.pendown()


for x in range(10):
    if x % 2 == 0:
        direction = 'right'
    else:
        direction = 'left'
    put_dots_on_line()
    change_line(direction)




t.Screen().exitonclick()