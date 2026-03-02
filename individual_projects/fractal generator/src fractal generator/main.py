#AS 2nd main file

import turtle
from Functions import fractalize, fractalize_2

screen = turtle.Screen()
screen.bgcolor('#aaaaaa')
t = turtle.Turtle()
t.pensize(1)
t.teleport(-600,-450)
t.left(60)
t.speed(0)
t.color('red')

print("Welcome")
while True:
    uinput = input("Would you like to 1: create a fractal, or 2: leave")
    if uinput == "1":
        while True:
            pass
    elif uinput == "2":
        break
    else:
        print("Invalid input.")
        continue
print("Goodbye")