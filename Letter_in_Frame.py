from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(0)
#tracer(100)

tom.color('cyan')
def flower():
	w=0.1
	for i in range(45):
		tom.fd(2)
		tom.rt(i/2)
		w=w+0.1
        
		tom.width(w)
	w=0.1
	tom.lt(130)
	for i in range(45):
		tom.fd(2)
		tom.lt(i/2)
		w=w+0.1
		tom.width(w)

for count in range (12):
	for i in range (3):
		flower()
		tom.width(0.1)
	tom.pu()
	tom.fd(80)
	tom.pd()
    

tom.pu()
tom.goto(-20,260)
tom.setheading(0)
tom.pd()

tom.color('gold')
w=(0.4)
tom.rt(90)
for i in range(18):
	tom.fd(10)
	tom.rt(i/4.5)
	w=w+0.3
	tom.width(w)
tom.rt(80)
tom.circle(-6,45)
tom.circle(-15,88)
tom.setheading(0)
tom.rt(10)
for i in range(11):
	tom.fd(8)
	tom.lt(i/2.5)
	w=w+0.2
	tom.width(w)

tom.hideturtle()
