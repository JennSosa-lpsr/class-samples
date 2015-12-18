import turtle
from Tkinter import *
# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()
myTurtle = turtle.Turtle()
def triangle(myTurtle):
	sidecount = 0
	while sidecount < 3:
        	myTurtle.forward(100)
        	myTurtle.right(120)
        	sidecount = sidecount + 1


# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda:shawn.penup())
pendown = Button(frame, text='pendown', command=lambda:shawn.pendown())
backward = Button(frame, text='backward', command=lambda:shawn.backward(50))
shape = Button(frame, text='shape', command=lambda:triangle.(shawn)
# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
backward.pack(side=LEFT)
shape.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
