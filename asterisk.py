# square.py

import turtle

# make our turtle

buzz = turtle.Turtle()


# buzz makes a square
buzz.color("blue")
buzz.left(180)
buzz.forward(200)
buzz.penup()
buzz.left(180)
buzz.pendown()
buzz.forward(250)
buzz.penup()
buzz.left(180)        
buzz.forward(90)
buzz.right(45)
buzz.pendown()
buzz.forward(100)
buzz.backward(200)
buzz.left(45)
buzz.penup()
buzz.forward(100)
buzz.right(120)
buzz.pendown()
buzz.forward(175)
# Wait to exit until I've clicked
turtle.exitonclick()





