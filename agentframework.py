# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:58:22 2017

@author: gyjehb
"""
#Imported functions
import random

#Creating the agent
class Agent():
    def __init__(self, environment,agents):
        self.agents = agents        
        '''self.sheep = sheep'''        
        self.x = random.randint(0,(len(environment[0])))
        self.y = random.randint(0,(len(environment)))
        self.environment = environment
        self.store = 0
        
#Setting the movement of agents within the environment        
    def move(self):
        if random.random() < 0.5:           
            self.x = (self.x +1) % len(self.environment[0])   
        else:
            self.x = (self.x -1) % len(self.environment[0])
                
        if random.random() < 0.5:
            self.y = (self.y +1) % len(self.environment[0])
        else:
            self.y = (self.y -1) % len(self.environment[0])
    
    
#Setting the consumption of agents    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10     
 
#Feeding into share_with_neighbours function
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        
#Communication behavoiural method for agents
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:                   # Loop through the agents in self.agents
            distance = self.distance_between(agent) # Calculate the distance between self and the current other agent:
            if distance ==0:
                break
            if distance <= neighbourhood:           # If distance is less than or equal to the neighbourhood
                sum = self.store + agent.store      # Sum self.store and agent.store
                avg=sum/2                           # Divide sum by two to calculate average
                self.store=avg                      # self.store = average
                agent.store=avg                     # agent.store = average
                
                          
#Print of information for the agent
    def __str__(self):
        return "sheep " + str(self.sheep) + " is at position "\
        + str(self.x) + str(self.y) + " has consumed "\
        + str(self.store)
        
        
#Agents eating without values & sicking up store
    def vom(self):
        if self.store > 1200:
            self.environment[self.x][self.y] += self.store
            self.store = 500
        
            
            
    
