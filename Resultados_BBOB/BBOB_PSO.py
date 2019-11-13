# PSO n-dimension algorithm that searches minimums
# Author: Borja Arroyo
# Version: 1.3

# Parameters
#   c1 = input
#   c2 = input
#   w = input


import random as rn
import numpy as np
import time

# Parameters
particles = 100
iterations = 100
w = 0.5
c1 = 2
c2 = 1
dimensions = 0

# Objective function definition (4-D)
def objective_function(a,b,c,d):
    return 2*a+a**2+b**2+c**2+d**2

# Initialize data structures
def initialize_structures(x0=None):
    global dimensions
    if x0 is not None:
        dimensions = x0.size
    else:
        dimensions = 4

    boundaries = []
    x = []
    v = []
    bip = []
    bsp = []
    for i in range(0,dimensions):
        # Add boundaries for each dimension
        boundaries.append((-5,5))
        # Position of each particle
        x.append(np.random.uniform(boundaries[i][0],boundaries[i][1],particles))
        # Velocity of each particle
        v.append(np.random.uniform(-abs(boundaries[i][1]-boundaries[i][0]),\
            abs(boundaries[i][1]-boundaries[i][0]),particles))
        # Best Individual Position
        bip.append(np.full(particles,np.inf))
        # Best Swarm Position
        bsp.append(np.inf)
    # Append elements to store fitness in last row/value
    bip.append(np.full(particles,np.inf))
    bsp.append(np.inf)
    return x,v,bip,bsp,boundaries

# Generate new speed and position values for each particle
def update_swarm(x,v,bip,bsp,boundaries):
    for i in range(0,particles):
        r1 = rn.uniform(0,1)
        r2 = rn.uniform(0,1)
        speed = []
        cognitive = []
        social = []
        for y in range(0,dimensions):
            speed.append(w * v[y][i])
            cognitive.append(c1 * r1 * (bip[y][i]-x[y][i]))
            social.append(c2 * r2 * (bsp[y]-x[y][i]))
            v[y][i] = speed[y] + cognitive[y] + social[y]
            x[y][i] = x[y][i] + v[y][i]
        if(x[y][i] < boundaries[y][0]):
            x[y][i] = boundaries[y][0]
        elif(x[y][i] > boundaries[y][1]):
            x[y][i] = boundaries[y][1]

def evaluate_swarm(x,bip,bsp,problem=None):
    for i in range(0,particles):
        fitness = 0.0
        current_x = []
        for y in range(0,dimensions):
            current_x.append(x[y][i])
        if problem is not None:
            fitness = problem(current_x)
        else:
            fitness = objective_function(current_x[0],current_x[1],current_x[2],current_x[3])
        if(fitness < bip[dimensions][i]):
            for y in range(0,dimensions):
                bip[y][i] = current_x[y]
            bip[dimensions][i] = fitness
        if(fitness < bsp[dimensions]):
            for y in range(0,dimensions):
                bsp[y] = current_x[y]
            bsp[dimensions] = fitness


def main(problem=None, x0=None):
    # t_ini = time.time()                                             
    x,v,bip,bsp,boundaries = initialize_structures(x0)
    evaluate_swarm(x,bip,bsp,problem)
    # print(bsp)
    for _ in range(0,iterations):
        update_swarm(x,v,bip,bsp,boundaries)
        evaluate_swarm(x,bip,bsp,problem)
        # print(bsp)

    # t_end = time.time()
    # print("Execution time: {}".format(t_end-t_ini))

    if problem is not None:
        return bsp[dimensions]


main()