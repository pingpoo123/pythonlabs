import turtle
import random

def random_step(turt):
    turt.forward(random.randint(5,15))
    r = random.randint(0,1)
    if r == 1:
        turt.left(45)
    else:
        turt.right(45)

def random_walk(turt,n):
    for i in range(n):
        random_step(turt)

#ninja = turtle.Turtle()
#random_walk(ninja, 10)
#turtle.mainloop()

turtle.Screen().delay(1)

t1 = turtle.Turtle()
t1.pencolor('blue')
t1.penup()
t1.goto(-50,-50)
t1.pendown()

t2 = turtle.Turtle()
t2.pencolor('red')
t2.penup()
t2.goto(50,50)
t2.pendown()

while t1.distance(t2) > 100:
    random_step(t1)
    random_step(t2)

turtle.mainloop()