# square.py

import turtle

# make our turtle

buzz = turtle.Turtle()


# buzz makes a square

lines = 0
while lines < 4:
	buzz.forward(150)
	buzz.left(90)
	lines = lines + 1

# Wait to exit until I've clicked
turtle.exitonclick()
