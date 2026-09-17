import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(30)

#i is an incrementor/iterator
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(5,70)

def more(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.right(5)
more(60)

turtle.done()



