import turtle, random

def choose_vertex():
    return random.randint(1,3)

def random_x():
    return random.uniform(0,4)
    
def random_y():
    return random.uniform(0,3.46)

def main():
    t = turtle.Turtle()
    turtle.setworldcoordinates(-1,-1,5,5)
    turtle.tracer(0)
    x=y=xt=yt=i=0
    K=10000

    # Set three default points
    t.setx(0)
    t.sety(0)
    t.forward(0.01)
    t.penup()

    t.setx(4)
    t.sety(0)
    t.pendown()
    t.forward(0.01)
    t.penup()

    t.setx(2)
    t.sety(3.46)
    t.pendown()
    t.forward(0.01)
    t.penup()

    # Set first random point
    t.setx(random_x())
    t.sety(random_y())
    t.pendown()
    t.forward(0.01)
    t.penup()

    while i<K:
        (xt,yt) = t.pos()
        point = choose_vertex()

        if point==1:
            x=0
            y=0
        elif point==2:
            x=4
            y=0
        else:
            x=2
            y=3.46
        
        # Get te mid point between the previous one and the triangle's vertex
        t.setx((xt+x)/2)
        t.sety((yt+y)/2)
        t.pendown()
        t.forward(0.01)
        t.penup()

        i+=1

    turtle.update()
    turtle.done()


main()



