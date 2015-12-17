# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors
 
# bring in the packages of functions we need
import random
import turtle
 
# -------- functions start here ----------------

# I created a list of colors to use for the shapes.
c = ['blue','red','yellow','purple','pink','black']
 
# We set a function to do a triangle.
def regular_triangle(myTurtle, x, y, side):
# We tell the turtle to pick up the pen.
        myTurtle.penup()
# We tell it to go to a certain coordinate.
        myTurtle.goto(x,y)
#We tell it to put the pen down after going there.
        myTurtle.pendown()
#We set a variable equal to 0.
        side_count = 0
# We let it choose a random color.
	myTurtle.color(random.choice(c))
# We set a loop to continue 3 times.
        while side_count < 3:
# We tell it to move that amount side.
                myTurtle.forward(side)
# We tell it to move exactly 120 degrees right.
                myTurtle.right(120)
 
# We ask it to add one to the variable so that it could loop.
               side_count = side_count + 1
 
# We now set a def statement to make a sqare.
def regular_square(myTurtle, x, y, side):
# We tell the turtle to not draw.
        myTurtle.penup()
# We tell the turtle to go to that coordinate.
	myTurtle.goto(x,y)
# We ask for the turtle to draw again.
	myTurtle.pendown()
# We set a variable equal to 0.
	sides = 0
# We let the command choose a random color for the shape.
	myTurtle.color(random.choice(c))

# We set a loop to run 4 times.
	while sides < 4:
# We tell the turtle to move side amount.
		myTurtle.forward(side)
# We tell the turtle to move left 90 degrees.
 		myTurtle.left(90)
# We add 1 to the variable so that the loop continues.
		sides = sides + 1
# We a def to make a pentagon.
def regular_pentagon(myTurtle, x, y, side):
# We ask the turtle to put the pen up.
        myTurtle.penup()
# We ask the turtle to go to a coordinate point.
	myTurtle.goto(x,y)
# We tell the turtle to put the pen down.
	myTurtle.pendown()
# We set a variable equal to 0.
	sides_count = 0
# We ask the turtle to choose a random color.
	myTurtle.color(random.choice(c))
# We set a loop to run 5 times.
	while sides_count < 5:
# We ask the turtle to move to the side.
		myTurtle.forward(side)
# We ask it to move 72 degrees left.
		myTurtle.left(72)
# We add 1 to the variable so that it keeps on running.
		sides_count = sides_count + 1
 
# We set a def to make a hexagon.
def regular_hexagon(myTurtle, x, y, side):
# We ask the turtle to pick up the pen.
        myTurtle.penup()
# We ask it to go to another coordinate pixel.
	myTurtle.goto(x,y)
# We ask the turtle to put the pen down.
	myTurtle.pendown()
# We set a variable equal to 0.
	sides_counts = 0
# We ask it to choose a random color.
	myTurtle.color(random.choice(c))
# We ask it to loop 6 times.
	while sides_counts < 6:
# We ask it to move forward sides.
		myTurtle.forward(side)
# We ask it to move 60 degrees left.
		myTurtle.left(60)
# We add 1 to the variable for it to keep running.
		sides_counts = sides_counts + 1
 
# We set a def to make an octagon.
def regular_octagon(myTurtle, x, y, side):
# We ask for it to put the pen up.
        myTurtle.penup()
# We tell it to go to a coordinate.
	myTurtle.goto(x,y)
# We ask for it to put the pen back down.
	myTurtle.pendown()
# We set a variable equal to 0.
	sidess = 0
# We let the command choose a random color for the shape.
	myTurtle.color(random.choice(c))
# We make a loop for it to run 8 times.
	while sidess < 8:
# We tell the turtle to move side amount.
		myTurtle.forward(side)
# We tell it to turn 45 degrees left.
		myTurtle.left(45)
# We add one to the variable to keep the loop going.
		sidess = sidess + 1
 
# we set a def function to make a circle.
def circle(myTurtle, x, y, radius):
# We ask it to pick up a pen.
        myTurtle.penup()
#Go to that coordinate.
	myTurtle.goto(x,y)
# Put the pen back down.
	myTurtle.pendown()
# Choose a random color.
	myTurtle.color(random.choice(c))
# We male the circle using the radius.
	myTurtle.circle(radius)
 
# -------- execution starts here ----------------
 
# We ask it to display this line.
print("Welcome to the random shape drawer!")
# It will display this.
print("You choose the shapes, and we choose the position, color, and size.")
 
# We create a new turtle.
squirt = turtle.Turtle()
 
# Shape is an empty varibale.
shape = ""
# We set a loop to ask the user for a shape.
while shape != "exit":
# We ask it to print this if it doesn't equal it.
        print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, and circle.")
# We ask it to display this.
        print("If you're done making shapes, just type 'exit'.")
# We turn their input into a variable.
        shape = raw_input()
 
# We let it choose a random number for the coordinate.
        randx = random.randint(-200,200)
#  We let it choose a random coordinate.
        randy = random.randint(-200,200)
# Choose a random coordinate between 5 and 100.
        randside = random.randint(5,100)
 
# We create make an if statement for the shapes.
        if shape == 'triangle':
# We put together those commands for the triangle.
                regular_triangle(squirt, randx, randy, randside)
# We set an else and if statement if they choose a square.
        elif shape == 'square':
# We set the commands together.
                regular_square(squirt, randx, randy, randside)
# We set an elif in case they choose a pentagon.
        elif shape == 'pentagon':
# We set all commands to the pentagon.
                regular_pentagon(squirt, randx, randy, randside)
# We set in elif for a hexagon.
        elif shape == 'hexagon':
# We set the commads together.
                regular_hexagon(squirt, randx, randy, randside)
# We set an elif if they choose an octagon.
        elif shape == 'octagon':
# All comands apply to octagon.
                regular_octagon(squirt, randx, randy, randside)
# We set an elif for the circle.
        elif shape == 'circle':
# We set the commands for the circle.
                circle(squirt, randx, randy, randside)

