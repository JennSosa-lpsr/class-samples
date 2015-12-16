import turtle

buzz = turtle.Turtle()

buzz.color("purple")
buzz.circle(100)
buzz.right(90)
buzz.forward(150)
buzz.shape("square")
buzz.stamp()
buzz.backward(250)
buzz.circle(50)
buzz.right(90)
buzz.pendown()
buzz.shape("circle")
buzz.forward(25)
buzz.stamp()
lines = 0
while lines < 3:
	buzz.forward(150)
	buzz.left(120)
	buzz.color("green")
	buzz.shape("turtle")
        lines = lines + 1
buzz.right(90)
buzz.color("gold")
buzz.shape("arrow")
buzz.forward(60)
buzz.stamp()
buzz.backward(120)
buzz.stamp()
turtle.exitonclick()
