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
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
	myTurtle.color(random.choice(c))
        while side_count < 3:
                myTurtle.forward(side)
                myTurtle.right(120)
                side_count = side_count + 1
 
def regular_square(myTurtle, x, y, side):
        myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	sides = 0
	myTurtle.color(random.choice(c))
	while sides < 4:
		myTurtle.forward(side)
 		myTurtle.left(90)
		sides = sides + 1
def regular_pentagon(myTurtle, x, y, side):
        myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	sides_count = 0
	myTurtle.color(random.choice(c))
	while sides_count < 5:
		myTurtle.forward(side)
		myTurtle.left(72)
		sides_count = sides_count + 1
 
def regular_hexagon(myTurtle, x, y, side):
        myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	sides_counts = 0
	myTurtle.color(random.choice(c))
	while sides_counts < 6:
		myTurtle.forward(side)
		myTurtle.left(60)
		sides_counts = sides_counts + 1
 
def regular_octagon(myTurtle, x, y, side):
        myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	sidess = 0
	myTurtle.color(random.choice(c))
	while sidess < 8:
		myTurtle.forward(side)
		myTurtle.left(45)
		sidess = sidess + 1
 
def circle(myTurtle, x, y, radius):
        myTurtle.penup()
	myTurtle.goto(x,y)
	myTurtle.pendown()
	myTurtle.color(random.choice(c))
	myTurtle.circle(radius)
 
# -------- execution starts here ----------------
 
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
 
squirt = turtle.Turtle()
 
shape = ""
while shape != "exit":
        print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, and circle.")
        print("If you're done making shapes, just type 'exit'.")
        shape = raw_input()
 
        randx = random.randint(-200,200)
        randy = random.randint(-200,200)
        randside = random.randint(5,100)
 
        if shape == 'triangle':
                regular_triangle(squirt, randx, randy, randside)
        elif shape == 'square':
                regular_square(squirt, randx, randy, randside)
        elif shape == 'pentagon':
                regular_pentagon(squirt, randx, randy, randside)
        elif shape == 'hexagon':
                regular_hexagon(squirt, randx, randy, randside)
        elif shape == 'octagon':
                regular_octagon(squirt, randx, randy, randside)
        elif shape == 'circle':
                circle(squirt, randx, randy, randside)

