import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(30)

def star(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)
star (5,70)

def more (iRange):
     length = 5
     for i in range(iRange):
            star(length, 144)
            length += 5
            t.right(5)
more(65)

turtle.done()