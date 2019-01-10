from turtle import *

tom = Turtle()
tom.shape('turtle')
tom.speed(0)
tom.width(2)
tom.color('#53aa58')

def sample():
	tom.circle(450,50)
	tom.lt(12)
	tom.circle(350,-70)
	tom.goto(0,0)

for i in range (13):
    sample()
    tom.lt(360.0/10)

tom.hideturtle()
