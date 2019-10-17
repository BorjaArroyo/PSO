# PSO 1-D Algorithm that searches minimums
# Author: Borja Arroyo
# Version: 1.0

# Parameters
#   c1 = c2 = 2
#   w = 0.9
#   boundaries = (-10,10)
#   particles = 100


from __future__ import (absolute_import, division, print_function, unicode_literals)
import random
import input

# Parameters
particles = 100
boundaries = (-10,10)
w = 0.5
c1 = 2
c2 = 2

# Objective function definition (1-D)
def objective_function(a):
    return 2*a+a**2

# Initialize position of each particle
def initialize_structures():
    for i in range(0,particles):
        x[i] = random.uniform(boundaries[0],boundaries[1])
        v[i] = random.uniform(-abs(boundaries[1]-boundaries[0]),abs(boundaries[1]-boundaries[0]))

# Generate new speed and position values for each particle
def update_swarm():
    for i in range(0,particles):
        r1 = random.uniform(0,1)
        r2 = random.uniform(0,1)
        speed = w * v[i]
        cognitive = c1 * r1 * (bip[i][0]-x[i])
        social = c2 * r2 * (bsp[0]-x[i])
        v[i] = speed + cognitive + social
        x[i] = x[i] + v[i]
        if(x[i] < boundaries[0]):
            x[i] = boundaries[0]
        elif(x[i] > boundaries[1]):
            x[i] = boundaries[1]

def evaluate_swarm():
    for i in range(0,particles):
        fitness = objective_function(x[i])
        if(fitness < bip[i][1]):
            bip[i][0] = x[i]
            bip[i][1] = fitness
        if(fitness < bsp[1]):
            bsp[0] = x[i]
            bsp[1] = fitness


# Initialization of data structures
v = [0 for i in range (0,particles)]                                # Velocity of each particle
x = [0 for i in range (0,particles)]                                # Position of each particle
bip = [[100 for i in range (0,2)] for y in range(0,particles)]      # Best Individual Position and its fitness
bsp = [100,100]                                                     # Best Swarm Position and its fitness

initialize_structures()
evaluate_swarm()
print(bsp)
for i in range(0,50):
    update_swarm()
    evaluate_swarm()
    print(bsp)