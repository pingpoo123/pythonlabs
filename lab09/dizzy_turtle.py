import turtle
from race_window import RaceWindow
from race_turtle import RaceTurtle
import random

class DizzyTurtle(RaceTurtle):
    
    def __init__(self, w, nbr):
        super().__init__(w, nbr)
        self.dizzy = random.randint(1, 5)
        self._w = w
    
    def race_step(self):
        if self.dizzy > random.randint(1,5):
            self.right(random.randint(-5,5) * self.dizzy)
        super().race_step()
        if self.ycor() < RaceWindow.get_start_Y(self._w, self._nbr) - 25:
            self.setheading(self.dizzy * 9)
        if self.ycor() > RaceWindow.get_start_Y(self._w, self._nbr) + 25:
            self.setheading(self.dizzy * -9)
    
    def __str__(self):
        return f'Nummer {self._nbr} - DizzyTurtle (Yrsel: {self.dizzy})'