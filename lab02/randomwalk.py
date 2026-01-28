import turtle
import random

ninja = turtle.Turtle()

steg = 100

for i in range(steg):
    r = random.randint(0,1)
    if r == 1:
        ninja.left(45)
    else:
        ninja.right(45)
    ninja.forward(10)

turtle.mainloop()