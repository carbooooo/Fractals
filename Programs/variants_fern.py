# Drawing barnsley fractal variants using python turtle

import turtle, random
turtle.setworldcoordinates(-5,-2,5,10)
t = turtle.Turtle()

x=y=n=xn=yn=0
turtle.tracer(0)
t.setx(0)
t.sety(0)
t.width(2)
t.color("green")
while n<500000:
    print(n)
    r = random.uniform(0,1)

    if r <0.02:
        xn = 0.0
        yn = 0.25*y-0.4
    elif r <0.86:
        xn = 0.95 * x + 0.005 * y - 0.002
        yn = -0.005 * x + 0.93 * y + 0.5
    elif r<0.93:
        xn = 0.035 * x - 0.2 * y -0.09
        yn = 0.16 * x + 0.04 * y + 0.02
    else:
        xn = -0.04 * x + 0.2 * y + 0.083
        yn = 0.16 * x + 0.04 * y + 0.12
    
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