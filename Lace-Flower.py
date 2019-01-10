from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.setheading(180)
tom.color('#db7884')
tom.speed(0)
tom.width(0.2)

def samp():
    r=8
    for count in range (60):
        tom.circle(r)
        r=r+6
    
for c in range (15):
    samp()
    tom.right(360.0/15)
