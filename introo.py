import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(2)

def equal(z):
    t.forward(z)
    t.left(120)
    t.forward(z)
    t.left(120)
    t.forward(z)
equal(90)

turtle.done()