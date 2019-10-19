# PSO 1-D algorithm that searches minimums
# Author: Borja Arroyo
# Version: 1.1

# Parameters
#   c1 = c2 = 2
#   w = 0.5


import random as rn
import numpy as np
import numba as nb
import time

# Parameters
particles = 100
w = 0.5
c1 = 2
c2 = 2
boundaries = (-10,10)

# Objective function definition (1-D)
def objective_function(a):
    return a**2

# Initialize data structures
def initialize_structures():
    x = np.random.uniform(boundaries[0],boundaries[1],particles)    # Position of each particle
    v = np.random.uniform(-abs(boundaries[1]-boundaries[0]),\
        abs(boundaries[1]-boundaries[0]),particles)                 # Velocity of each particle
    bip = np.full((particles,2),np.inf)                             # Best Individual Position
    bsp = np.full(2,np.inf)                                         # Best Swarm Position
    return x,v,bip,bsp

# Generate new speed and position values for each particle
#@nb.njit()
def update_swarm(x,v,bip,bsp):
    for i in range(0,particles):
        r1 = rn.uniform(0,1)
        r2 = rn.uniform(0,1)
        speed = w * v[i]
        cognitive = c1 * r1 * (bip[i][0]-x[i])
        social = c2 * r2 * (bsp[0]-x[i])
        v[i] = speed + cognitive + social
        x[i] = x[i] + v[i]
        if(x[i] < boundaries[0]):
            x[i] = boundaries[0]
        elif(x[i] > boundaries[1]):
            x[i] = boundaries[1]

def evaluate_swarm(x,bip,bsp,problem=None):
    for i in range(0,particles):
        fitness = 0.0
        if problem is not None:
            fitness = problem(x[i])
        else:
            fitness = objective_function(x[i])
        if(fitness < bip[i][1]):
            bip[i][0] = x[i]
            bip[i][1] = fitness
        if(fitness < bsp[1]):
            bsp[0] = x[i]
            bsp[1] = fitness


def main(problem=None):
    t_ini = time.time()                                             
    x,v,bip,bsp = initialize_structures()
    evaluate_swarm(x,bip,bsp,problem)
    print(bsp)
    for i in range(0,10):
        update_swarm(x,v,bip,bsp)
        evaluate_swarm(x,bip,bsp)
        print(bsp)

    t_end = time.time()
    print("Execution time: {}".format(t_end-t_ini))

    if problem is not None:
        return bsp[0]


main()