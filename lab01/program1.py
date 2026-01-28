#Laboration 1: approximera en matematisk konstant

import random

n=0
iterations=1000000

for k in range(iterations):
    x=random.random()
    #print(x)
    y=random.random()
    if x**2+y**2<1:
        n=n+1

ratio=n/iterations
print(4*ratio)

ord = 'hejsan'

d = {
    'ta': 5
}
print(d['ta'])
for t in d:
    print(t)