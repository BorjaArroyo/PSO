# PSO 1-D parallelized algorithm that searches minimums
# Author: Borja Arroyo
# Version: 1.1

# Parameters
#   c1 = c2 = 2
#   w = 0.5
#   particles = 100


import random as rn
import numpy as np
import numba as nb

# Parameters
particles = 100
w = 0.5
c1 = 2
c2 = 2
boundaries = (-10,10)

# Objective function definition (1-D)
def objective_function(a,b):
    return a**2

# Initialize position of each particle
def initialize_structures(v,x):
    x = np.random(boundaries[0],boundaries[1])
    v = np.random(-abs(boundaries[1]-boundaries[0]),abs(boundaries[1]-boundaries[0]))

# Generate new speed and position values for each particle
def update_swarm(v,x,bip,bsp):
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

def evaluate_swarm(v,x,bip,bsp,problem):
    for i in range(0,particles):
        fitness = problem(x[i])
        if(fitness < bip[i][1]):
            bip[i][0] = x[i]
            bip[i][1] = fitness
        if(fitness < bsp[1]):
            bsp[0] = x[i]
            bsp[1] = fitness

def main(problem):
    # Initialization of data structures
    v = [0 for i in range (0,particles)]                                # Velocity of each particle
    x = [0 for i in range (0,particles)]                                # Position of each particle
    bip = [[100 for i in range (0,2)] for y in range(0,particles)]      # Best Individual Position and its fitness
    bsp = [100,100]                                                     # Best Swarm Position and its fitness
    boundaries = 


    initialize_structures(v,x)
    evaluate_swarm(v,x,bip,bsp,problem)
    print(bsp)
    for i in range(0,50):
        update_swarm(v,x,bip,bsp)
        evaluate_swarm(v,x,bip,bsp,problem)
        print(bsp)

    return bsp

if __name__=="__main__":
    main()