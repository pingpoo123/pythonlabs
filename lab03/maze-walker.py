import maze
import turtle

val = int(input('Välj en labyrint 1 till 5:\n'))
m = maze.Maze(val)
turtle.delay(1)
if val == 5:
    turtle.Screen().tracer(2)

walker = turtle.Turtle()
walker.shape("turtle")
walker.shapesize(0.75)

walker.penup()
walker.goto(m.entry())
walker.setheading(90)
walker.pendown()

while not m.at_exit(walker.pos()):
    if not m.wall_at_left(walker.heading(), walker.pos()):
        walker.left(90)
    elif m.wall_in_front(walker.heading(), walker.pos()):
        walker.right(90)
    walker.forward(1)

turtle.mainloop()
