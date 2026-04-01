import turtle
from race_window import RaceWindow
import random

class RaceTurtle(turtle.Turtle):
    
    def __init__(self, w, nbr):
        super().__init__()
        self._nbr = nbr
        self.penup()
        self.goto(RaceWindow.get_start_X(w, self._nbr), RaceWindow.get_start_Y(w, self._nbr))
        self.pendown()
        self.setheading(0)

    def race_step(self):
        self.forward(random.randint(1, 6))

    def __str__(self):
        return f'Nummer {self._nbr}'
