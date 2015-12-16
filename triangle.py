# square.py

import turtle

buzz = turtle.Turtle()



lines = 0
while lines < 3:
        buzz.forward(150)
        buzz.left(120)
        lines = lines + 1

# Wait to exit until I've clicked
turtle.exitonclick()


