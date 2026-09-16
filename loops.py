import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(10)

sidelength = 5
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
    t.right(5)
square(5,90)

def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
    t.right(5)
addSquares(60)

turtle.done()



