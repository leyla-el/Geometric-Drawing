from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(0)
tom.width(4)
tom.tracer(100)


colorBox = ['#9eb539', '#b2b3e8', '#7b98f7', '#3d4c07']

side=30
u=20

for i in range (200):
	for count in range (4):
		tom.color( colorBox [count] )
		tom.forward(side)
	side = side + u
	u=-u
	tom.penup()
	tom.goto(0,0)
	tom.lt(360.0/200)
	tom.pendown()
    
tom.hideturtle()
