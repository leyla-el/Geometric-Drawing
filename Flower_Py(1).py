from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(0)
tom.color('#fc1631')

def flower():
	for j in range (20):
		w=0.01
		for i in range(52):
			tom.fd(12)
			tom.lt(i)
			w=w+0.05
			tom.width(w)
		tom.pu()
		tom.goto(0,0)
		tom.setheading(0)
		tom.pd()
		tom.lt((j+1)*(360.0/20))

flower()
tom.fd(12)

tom.hideturtle()
