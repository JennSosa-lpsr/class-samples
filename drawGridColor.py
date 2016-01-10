import turtle

def drawSquareRow(myTurtle):
	number = 0
	while number < 5:
		drawSquare(myTurtle)
		buzz.penup()
	        buzz.left(90)
        	buzz.forward(15)
       		buzz.left(90)
		buzz.pendown()
		number = number + 1
		

def drawSquare(myTurtle):
	count = 0
	while count < 4:
		myTurtle.color("red")
		myTurtle.forward(20)
		myTurtle.left(90)
		count = count + 1
	myTurtle.forward(20)	
	counts = 0
	while counts < 4:
		myTurtle.color("blue")
		myTurtle.forward(20)
		myTurtle.left(90)
		counts = counts + 1
	myTurtle.forward(20)
	myTurtle.right(90)	
	counting = 0
	while counting < 4:
		myTurtle.color("green")
		myTurtle.forward(20)
		myTurtle.right(90)
		counting = counting + 1

	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	numy = 0
	while numy < 4:
		myTurtle.color("yellow")
		myTurtle.forward(20)
		myTurtle.right(90)
		numy = numy + 1



buzz = turtle.Turtle()
num = 0
while num < 1:
	drawSquareRow(buzz)
	num = num + 1
turtle.exitonclick()
