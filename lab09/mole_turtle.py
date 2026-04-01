import turtle
from race_window import RaceWindow
from race_turtle import RaceTurtle
import random

class MoleTurtle(RaceTurtle):
    
    def __init__(self, w, nbr):
        super().__init__(w, nbr)
    
    def race_step(self):
        r = random.randint(0,1)
        if r > 0: self.penup()
        else: self.pendown()
        super().race_step()

    def __str__(self):
        return f'Nummer {self._nbr} - Mullvad'