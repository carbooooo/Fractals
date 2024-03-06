# Drawing barnsley fractal using python turtle

import turtle, random
turtle.setworldcoordinates(-5,0,5,10)
t = turtle.Turtle()

x=y=n=xn=yn=0
turtle.tracer(0)
t.setx(0)
t.sety(0)
t.width(2)

while n<500000:
    r = random.uniform(0,1)

    if r <0.01:
        xn = 0.0
        yn = 0.16*y
    elif r <0.86:
        xn = 0.85 * x + 0.04 * y
        yn = -0.04 * x + 0.85 * y + 1.6
    elif r<0.93:
        xn = 0.2 * x - 0.26 * y
        yn = 0.23 * x + 0.22 * y + 1.6 
    else:
        xn = -0.15 * x + 0.28 * y
        yn = 0.26 * x + 0.24 * y + 0.44
    
    t.penup()
    t.setx(xn)
    t.sety(yn)
    t.pendown()
    t.forward(0.01)
    x=xn
    y=yn
    n+=1
    
turtle.update()
turtle.done()