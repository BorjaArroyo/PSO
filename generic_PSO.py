# PSO n-dimension algorithm that searches maximus or minimums
# Author: Borja Arroyo
# Version: 1.4

# Parameters
#   c1 = input
#   c2 = input
#   w = input

import sys
import random as rn
import numpy as np
import time

# Parameters
particles = 100
iterations = 100
# w = input('Choose the weight assigned to the previous step velocity\n')
# c1 = input('Choose the weight assigned to the best individual position\n')
# c2 = input('Choose the weight assigned to the best swarm position\n')
w = 0.5
c1 = 2
c2 = 2

# Objective function definition (4-D)
def objective_function(a):
    res = 0.0
    for elem in a:
        res +=elem**2
    return res
# Initialize data structures
def initialize_structures(dimensions,mode,restrictions=None):
    inicialization_value = 0.0
    if mode == 1:
        inicialization_value = -sys.maxsize
    else:
        inicialization_value = sys.maxsize

    x = []
    v = []
    bip = []
    bsp = []

    if restrictions == None:
        restrictions = []
        for i in range(0,dimensions+1):
            restrictions.append((-np.inf,np.inf))

    for i in range(0,dimensions):
        # Position of each particle
        x.append(np.random.uniform(restrictions[i][0],restrictions[i][1],particles))
        # Velocity of each particle
        v.append(np.random.uniform(-abs(restrictions[i][1]-restrictions[i][0]),\
            abs(restrictions[i][1]-restrictions[i][0]),particles))
        # Best Individual Position
        bip.append(np.full(particles,inicialization_value))
        # Best Swarm Position
        bsp.append(inicialization_value)
    # Append elements to store fitness in last row/value
    bip.append(np.full(particles,inicialization_value))
    bsp.append(inicialization_value)
    return x,v,bip,bsp

# Generate new speed and position values for each particle
def update_swarm(x,v,bip,bsp,dimensions,restrictions=None):
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

        if restrictions is not None:
            if(x[y][i] < restrictions[y][0]):
                x[y][i] = restrictions[y][0]
            elif(x[y][i] > restrictions[y][1]):
                x[y][i] = restrictions[y][1]

def evaluate_swarm(x,bip,bsp,function,mode,dimensions,restrictions=None):
    for i in range(0,particles):
        fitness = 0.0
        current_x = []
        for y in range(0,dimensions):
            current_x.append(x[y][i])
        
        fitness = function(current_x)
        if restrictions is not None:
            if fitness < restrictions[dimensions][0] or fitness > restrictions[dimensions][1]:
                return
        
        if mode == 0:
            if fitness < bip[dimensions][i]:
                for y in range(0,dimensions):
                    bip[y][i] = current_x[y]
                bip[dimensions][i] = fitness

            if(fitness < bsp[dimensions]):
                for y in range(0,dimensions):
                    bsp[y] = current_x[y]
                bsp[dimensions] = fitness

        else:
            if fitness > bip[dimensions][i]:
                for y in range(0,dimensions):
                    bip[y][i] = current_x[y]
                bip[dimensions][i] = fitness

            if(fitness < bsp[dimensions]):
                for y in range(0,dimensions):
                    bsp[y] = current_x[y]
                bsp[dimensions] = fitness


# If mode == 0, minimum search
# Else, maximum search
def main(dimensions,benchmarking,function,mode,restrictions=None):
    if benchmarking is True:
        t_ini = time.time()

    x,v,bip,bsp = initialize_structures(dimensions,mode,restrictions)
    evaluate_swarm(x,bip,bsp,function,mode,dimensions,restrictions)
    # print(bsp)
    for _ in range(0,iterations):
        update_swarm(x,v,bip,bsp,dimensions,restrictions)
        evaluate_swarm(x,bip,bsp,function,mode,dimensions,restrictions)
        # print(bsp)

    if benchmarking is True:
        t_end = time.time()
        print("Execution time: {}".format(t_end-t_ini))

    return bsp[dimensions]

res = [(-5,5),(-5,5),(-5,5),(-5,5),(-np.inf,np.inf)]
print(main(4,False,objective_function,0,restrictions=res))