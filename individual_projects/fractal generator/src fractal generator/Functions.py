#AS 2nd functions for fractal generator

import turtle
screen = turtle.Screen()
screen.bgcolor('#aaaaaa')
t = turtle.Turtle()
t.pensize(1)
t.teleport(-450,-300)
t.left(60)
t.speed(0)

def fractalize():
    for x in range(3):
        if x == 0:
            for i in range(3):
                t.forward(25)
                t.right(120)
            t.forward(25)
        elif x == 1:
            for i in range(3):
                t.forward(25)
                t.right(120)  
            t.forward(25)
            t.right(120)
            t.forward(25)
        elif x == 2:
            for i in range(3):
                t.forward(25)
                t.right(120)
            t.left(120*2)
            t.forward(25)
            t.right(120)
            t.forward(25)
            pass

def fractalize_2(num):
    current = num
    move = 2
    for i in range(current):
        move = move * 2

    if current == 1:
        for a in range(3):
            if a == 0:
                fractalize()
            elif a == 1:
                fractalize()
            else:
                t.right(120)
                t.forward(25*(2))
                fractalize()
                t.right(180)
                t.forward(25*(4))
                t.right(60)
                
    else:
        for a in range(3):
            if a == 0:
                fractalize_2(current-1)
            elif a == 1:
                fractalize_2(current-1)
            else:
                t.right(120)
                t.forward(25*(move/2))
                fractalize_2(current-1)
                t.right(180)
                t.forward(25*(move))
                t.right(60)

fractalize_2(4)

turtle.done()