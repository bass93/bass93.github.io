#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:21:15 2017

@author: jamesbass
"""

# -*- coding: utf-8 -*-

#Imported functions
import random
import agentframework
import matplotlib.pyplot
import matplotlib.animation
import csv


#Environment list 
environment = []
f = open ('in.txt', newline='')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:				    
        rowlist=[]
        for value in row:                   
            rowlist.append(value)
        environment.append(rowlist)
f.close()


#Number of agents & number of spaces moved (iterations) 
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 5
agents = []

#Animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

#Animation update
def update(frame_number):
    fig.clear()
    for j in range(num_of_iterations):
        random.shuffle (agents)
        matplotlib.pyplot.xlim(0,(len(environment[0])))
        matplotlib.pyplot.ylim(0,(len(environment)))
        
    
#    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].vom()
        agents[i].share_with_neighbours(neighbourhood)
        
#Agent framework link
        matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
#Running animation/plot
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
fig.show()
        














