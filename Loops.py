"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
bob = turtle.Turtle()

for i in range(100):
    bob.forward(11)
    bob.left(3.6)
