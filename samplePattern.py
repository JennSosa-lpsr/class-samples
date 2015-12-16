# samplePattern.py

# my turtle is a Turtle object
# my side is the length of a side in points. 
import turtle
 
def makeTriangle(myTurtle, side):
        myTurtle.forward(side)
	myTurtle.left(120)
	myTurtle.forward(side)
        myTurtle.left(120)
	myTurtle.forward(side)
        myTurtle.left(120)
 
# make our turtle
kipp = turtle.Turtle()
kipp.forward(150)
kipp.right(180)
 
# kipp makes triangles centered at a point that shifts
# and decreases in size with each loop
length = 100
while length > 0:
        makeTriangle(kipp, length)
        kipp.forward(3)
# makes the sides shorter
        length = length - 1
 
# wait to exit until I've clicked
turtle.exitonclick()

