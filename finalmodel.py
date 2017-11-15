#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:21:15 2017

@author: jamesbass
"""

# -*- coding: utf-8 -*-

#   Imported functions
import random
import agentframework
import matplotlib.pyplot
import matplotlib.animation
import csv


#   Number of agents & number of spaces moved (iterations) 
num_of_agents = 10
num_of_iterations = 1000
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


#   Setting the animation display (with fixed axis & grid extents)
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#   Making the agents (set within the environment extents)
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents, colours[i]))     


#   Moving agents (set to be random per iteration)
def update(frame_number):
    fig.clear()
    for j in range(num_of_iterations):
        random.shuffle (agents)
        matplotlib.pyplot.xlim(0,(len(environment[0])))
        matplotlib.pyplot.ylim(0,(len(environment)))
        
    
#   Loading in the agent functions    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].vom()
        agents[i].share_with_neighbours(neighbourhood)
    
    
#   Plotting the agents (including their colour properties) within the environment 
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color=agents[i].colour)    


#   Running animation/plot
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
fig.show()
#   Stopping condition of the model is set to the number of iterations (which is 1000)
