# PSO n-dimension algorithm that searches maximus or minimums
# Author: Borja Arroyo
# Version: 1.4

# Parameters
#   c1 = input
#   c2 = input
#   w = input

import sys
import random
import numpy as np
import time
import math

# Parameters
PARTICLES = 100
ITERATIONS = 100
# w = input('Choose the weight assigned to the previous step velocity\n')
# c1 = input('Choose the weight assigned to the best individual position\n')
# c2 = input('Choose the weight assigned to the best swarm position\n')
w = 0.5
c1 = 2
c2 = 2


class Particle:

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.position = []
        self.v_to_0 = []
        self.v_to_1 = []
        self.v_c = []
        self.best = ([], 0, 0)
        for _ in range(dimensions):
            r = random.randint(0, 1)
            self.position.append(r)
            self.v_to_0.append(random.random())
            self.v_to_1.append(random.random())
            self.v_c.append(0)
            self.best[0].append(0)

        self.fitness = 0
        self.weight = 0

    def evaluate(self, problem):
        fitness = 0
        weight = 0
        for i in range(self.dimensions):
            fitness += self.position[i]*problem.objects[i].gain
            weight += self.position[i]*problem.objects[i].weight

        self.fitness = fitness
        self.weight = weight

        while self.weight > problem.MAX_WEIGHT:
            self.adjust_position(problem)

        if self.fitness > self.best[1]:
            self.best = (self.position.copy(), self.fitness, self.weight)

    def adjust_position(self,problem):
        r = random.randint(0,self.dimensions-1)
        self.position[r] = 0
        self.fitness -= problem.objects[r].gain
        self.weight -= problem.objects[r].weight


class Swarm:

    def __init__(self, problem):
        self.particles = []
        self.problem = problem
        self.best = ([], 0, 0)
        self.dimensions = problem.dimensions
        for _ in range(PARTICLES):
            p = Particle(self.dimensions)
            self.particles.append(p)

        for _ in range(self.dimensions):
            self.best[0].append(0)

        self.evaluate()

    def evaluate(self):
        for p in self.particles:
            p.evaluate(self.problem)
            if p.best[1] > self.best[1]:
                self.best = p.best

    def update(self):
        for p in self.particles:
            di0 = 0
            di1 = 0
            dg0 = 0
            dg1 = 0
            for i in range(self.dimensions):
                r1 = random.random()
                r2 = random.random()
                if p.best[0][i] == 1:
                    di0 = -c1*r1
                    di1 = -di0
                else:
                    di0 = c1*r1
                    di1 = -di0

                if self.best[0][i] == 1:
                    dg0 = -c2*r2
                    dg1 = -di0
                else:
                    dg0 = c2*r2
                    dg1 = -di0

                p.v_to_0[i] = w*p.v_to_0[i] + di0 + dg0
                p.v_to_1[i] = w*p.v_to_1[i] + di1 + dg1

                if p.position[i] == 0:
                    p.v_c[i] = p.v_to_1[i]
                else:
                    p.v_c[i] = p.v_to_0[i]

                r3 = random.random()
                v_norm = 1/(1+math.e**-p.v_c[i])
                if r3 < v_norm:
                    p.position[i] = int(not p.position[i])

        self.evaluate()


def main(problem):
    s = Swarm(problem)

    for _ in range(ITERATIONS):
        s.update()

    print(s.best)

