#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:20:15 2017

@author: jamesbass
"""

import random
import agentframework
import matplotlib.pyplot
import matplotlib.animation
import csv


#   Number of agents & number of spaces moved (iterations) 
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 5
agents = []
environment = []
colours = ['red', 'blue', 'yellow', 'white', 'green', 'purple', 'grey', 'black', 'brown', 'magenta']
# Colours assinged to each individual agent (making it visually easier to track movement)


#   The imported dataset forming the environment (creating a 2-D list)
f = open ('in.txt', newline='')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:				    
        rowlist=[]
        for value in row:                   
            rowlist.append(value)
        environment.append(rowlist)
f.close()


#   Making the agents (set within the environment extents)
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents, colours[i])) 


#   Moving agents (set to be random per iteration)
for j in range(num_of_iterations):
        random.shuffle (agents)
        matplotlib.pyplot.xlim(0,(len(environment[0])))
        matplotlib.pyplot.ylim(0,(len(environment)))
        
        
#   Agent functions    
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)


#   Plotting the agents & environment
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y) 
matplotlib.pyplot.show()


#   Exporting the environment as a csv
f2 = open('environment.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
        writer.writerow(row)
f2.close()













