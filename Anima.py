from turtle insert *
tom = Turtle()
sc = Screen()
tom.shape('turtle')
tom.speed(0)
tom.color('#f47a42')
sc.tracer(1000)

def flower():
	w=1.2
	tom.width(w)
	for i in range(40):
		tom.fd(3.6)
		tom.lt(i/0.3)
		w=w+0.05
		tom.width(w)
	w=0.5
	tom.width(w)
	for i in range(40):
		tom.fd(3)
		tom.rt(i/0.3)
		w=w+0.1
		tom.width(w)

for c in range(10):
	tom.color('#f47a42')
	#tom.tracer(1000)
	for rad in range (10):
		for count in range (5):
			flower()
		tom.pu()
		tom.goto(0,0)
		tom.pd()
		tom.lt(360.0/10)
	tom.pu()
	tom.goto(0,0)
	tom.pd()   
	tom.color('black')
	for rad in range (10):
		for count in range (5):
			flower()
		tom.pu()
		tom.goto(0,0)
		tom.pd()
		tom.lt(360.0/10)
	tom.update()
        
tom.hideturtle()

