import random
from time import sleep

SLEEPY_TIME = 0.18

with open('satansNutsack.txt') as input_file:
    all_that_is_unholy = [line.strip() for line in input_file]

def String_Space_Generator(integer):
    return " " * integer

UP = [1,2,3,4,7,10,13,16,17,18,19] # Integer Wave Approximation
ACTUALLY_UP = []

for i in UP:
    ACTUALLY_UP.append(String_Space_Generator(i))

ACTUALLY_DOWN = list(reversed(ACTUALLY_UP))
INFINITY_IS_BIG = True

while INFINITY_IS_BIG:
    for space in ACTUALLY_UP:
        print(space + str(random.choice(all_that_is_unholy)))
        sleep(SLEEPY_TIME)
    for space in ACTUALLY_DOWN:
        print(space + random.choice(all_that_is_unholy))
        sleep(SLEEPY_TIME)
