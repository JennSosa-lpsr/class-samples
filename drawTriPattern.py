import turtle

import random
def drawRowTriangle(myTurtle):
	count = 0
	while count < 4:
		drawTriangle(myTurtle)
		myTurtle.penup()
		myTurtle.forward(30)
		myTurtle.pendown()
		count = count + 1


def drawTriangle(myTurtle):
	count = 0
	while count < 3:
		myTurtle.forward(10)
		myTurtle.left(120)
		count = count + 1
buzz = turtle.Turtle()
count = 0
while count < 3:
	drawRowTriangle(buzz)			
	buzz.penup()
	buzz.goto(0,0)
	buzz.pendown()
	buzz.left(20)
	count = count + 1
counts = 0
buzz.left(120)
while counts < 3:
	drawRowTriangle(buzz)
        buzz.penup()
        buzz.goto(0,0)
        buzz.pendown()
        buzz.left(20)
        counts = counts + 1


turtle.exitonclick()
