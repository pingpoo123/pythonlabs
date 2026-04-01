import turtle
from race_window import RaceWindow
from race_turtle import RaceTurtle
import random

class AbsentmindedTurtle(RaceTurtle):

    def __init__(self, w, nbr):
        super().__init__(w, nbr)
        self.absness = random.randint(1, 99)

    def race_step(self):
        if random.randint(1,100) > self.absness:
            super().race_step()
    
    def __str__(self):
        return f'Nummer {self._nbr} - AbsentmindedTurtle({self.absness}% Frånvarande)'