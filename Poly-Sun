from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(100)
tom.color ('orange')


def square(side):
	tom.begin_fill()
	for i in range (4):
		tom.lt(90)
		tom.fd(side)
	tom.end_fill()

def samp():
    side=40
    while side>0:
        tom.lt(45)
        square(side)
        side=side-5
        tom.penup()
        tom.rt(45)
        v=(side**2+side**2)**0.5
        tom.fd(v)
        tom.pd()
    tom.hideturtle()	
    
for k in range (25):
    samp()
    tom.goto(0,0)
    tom.lt(360.0/25)
