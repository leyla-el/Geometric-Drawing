from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(0)
tom.color('#12c99e')

def flower():
	for j in range (1):
		w=1.2
		tom.width(w)
		for i in range(38):
			tom.fd(3.6)
			tom.lt(i/0.5)
			w=w+0.05
			tom.width(w)
	for j in range (1):
		w=0.5
		tom.width(w)
		for i in range(38):
			tom.fd(3)
			tom.rt(i/10)
			w=w+0.1
			tom.width(w)


for count in range (8):
	flower()
        
tom.hideturtle()
