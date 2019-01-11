from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(0)
tom.goto(-100,0)

def flower():
	w=0.1
	for i in range(27):
		tom.fd(5)
		tom.lt(i+5)
		w=w+0.2
		tom.width(w)
	tom.circle(50,10)
	tom.circle(50,-10)
	w=0.1
	for i in range(27):
		tom.fd(5)
		tom.rt(i+5)
		w=w+0.1
		tom.width(w)


def frame():
	for t in range (4):
		for count in range (2):
			flower()
		tom.lt(90)

tom.color('orange red')
frame()

tom.pu()
tom.fd(250)
tom.pd()

tom.color('cyan')
frame()

tom.hideturtle()
