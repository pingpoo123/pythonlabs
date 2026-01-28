import turtle

k = 9

ninja = turtle.Turtle()

for i in range(k):
    ninja.forward(50)
    ninja.left(140)
    ninja.forward(50)
    ninja.right(100)

turtle.mainloop()