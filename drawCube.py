import turtle


def drawRhombus(myTurtle):
	count = 0
        myTurtle.left(30)
        while count < 4:
                myTurtle.fillcolor("blue")
		myTurtle.begin_fill()
		myTurtle.forward(20)
                myTurtle.left(120)
                myTurtle.forward(20)
                myTurtle.left(60)
		myTurtle.end_fill()
                count = count + 1
        myTurtle.right(120)
        myTurtle.fd(20)
        myTurtle.left(90)
	number = 0
        myTurtle.left(90)
        while number < 4:
                myTurtle.fillcolor("azure4")
                myTurtle.begin_fill()
                myTurtle.forward(20)
                myTurtle.left(60)
                myTurtle.forward(20)
                myTurtle.left(120)
                myTurtle.end_fill()
                number = number + 1



	num = 0
	myTurtle.right(60)
	while num < 4:
		myTurtle.fillcolor("aquamarine")
		myTurtle.begin_fill()
		myTurtle.forward(20)
		myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.left(120)
		myTurtle.end_fill()
		num = num + 1
	myTurtle.right(30)
def drawCube(myTurtle):
        numy = 0
        while numy < 4:
                drawRhombus(myTurtle)
                myTurtle.pu()
                myTurtle.right(30)
                myTurtle.forward(20)
                myTurtle.left(30)
                myTurtle.pd()
                numy = numy + 1
def drawCubeRows(myTurtle):
        counting = 0
        while counting < 5:
                drawCube(myTurtle)
                myTurtle.pu()
                myTurtle.left(150)
                myTurtle.fd(20)
                myTurtle.right(30)
                myTurtle.forward(140)
                myTurtle.left(90)
                myTurtle.forward(20)
                myTurtle.right(210)
                myTurtle.pd()
                counting = counting + 1

buzz = turtle.Turtle()
drawCubeRows(buzz)
turtle.exitonclick()


