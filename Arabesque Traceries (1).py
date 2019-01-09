from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(0)

def hexa():
	tom.color('olivedrab')
	for i in range (2):
		tom.width(4.5)
		tom.fd(30)
		tom.lt(60)
	tom.color('pale green')
	for j in range (4):
		tom.fd(6)
		tom.width(3)
		tom.fd(6)
		tom.width(2)
		tom.fd(18)
		tom.lt(60)
        
def flower(nom,dis):        
	for count in range (nom):
		tom.pu()
		tom.fd(dis)
		tom.pd()
		hexa()
		tom.pu()
		tom.goto(0,0)
		tom.pd()
		tom.lt(360.0/nom)

flower(10,15)
flower(16,85)
flower(22,145)


tom.hideturtle()  
