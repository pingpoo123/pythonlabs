from race_window import RaceWindow
from absentminded_turtle import AbsentmindedTurtle
from dizzy_turtle import DizzyTurtle
from mole_turtle import MoleTurtle

import random

w = RaceWindow()
racers = []
for i in range(8):
    n = i + 1
    type = random.randint(1,3)
    if type == 1:
        racers.append(AbsentmindedTurtle(w, n))
    elif type == 2:
        racers.append(DizzyTurtle(w, n))
    else:
        racers.append(MoleTurtle(w, n))
    print(racers[i].__str__())

podium = []
while True:
    for r in racers:
        if r.xcor() < RaceWindow.X_END_POS:
            r.race_step()
        elif podium.count(r) < 1:
            podium.append(r)

    if len(podium) == len(racers):
        break

for i in range(3):
    print(f'På plats {i + 1}: {podium[i].__str__()}')

