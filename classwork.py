import turtle

import random

c = ['blue','green','pink','yellow','red','purple']
tommy = turtle.Turtle()

count = 10
while count > 0:
	tommy.color(random.choice(c))
	tommy.forward(count * 30)
	tommy.left(120)
	count = count - 1		
turtle.exitonclick()
