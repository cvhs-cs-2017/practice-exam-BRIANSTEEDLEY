""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""
import turtle


smiles = turtle.Turtle()

smiles.speed(5)

smiles.begin_fill()
smiles.color("BLUE")
smiles.penup()
smiles.goto(0,-35)
smiles.pendown()
smiles.circle(140, 360)
smiles.end_fill()


smiles.begin_fill()
smiles.color('Black')
smiles.penup()
smiles.goto(-75,150)
smiles.pendown()
smiles.circle(10)
smiles.end_fill()

smiles.begin_fill()
smiles.penup()
smiles.goto(75,150)
smiles.pendown()
smiles.circle(10)
smiles.end_fill()


smiles.penup()
smiles.goto(0,0)
smiles.pendown()
smiles.circle(100,90)


smiles.penup()
smiles.setheading(180)
smiles.goto(0,0)
smiles.pendown()
smiles.circle(-100,90)
