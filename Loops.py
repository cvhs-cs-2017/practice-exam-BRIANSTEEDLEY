"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""

import Turtle
def reset():
    turtle.clear()
    turtle.pu()
    turtle.home()
    turtle.pd()

x = 100
y = 100
theta = 100
def triangle (x,y,theta):
    for i in range(1):
        turtle.pu()
        turtle.goto(-100,100)
        turtle.pd()
        turtle.forward(x)
        turtle.right(y)
        turtle.forward(theta)
        turtle.goto(-100,100)


triangle(x,y,theta)
