# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:58:22 2017

@author: gyjehb
"""
#   Imported functions
import random


#   Creating the agents, their properties & setting their positions randomly within the environment (using init method)
class Agent():
    def __init__(self, environment,agents, colour):
        self.agents = agents        
        self.x = random.randint(0,(len(environment[0])))
        self.y = random.randint(0,(len(environment)))
        self.environment = environment
        self.store = 0
        self.colour = colour                   
        
        
#   Setting the movement of agents (randomly & limited to one step) within the environment    
    def move(self):
        if random.random() < 0.5:           
            self.x = (self.x +1) % len(self.environment[0])   
        else:
            self.x = (self.x -1) % len(self.environment[0])
                
        if random.random() < 0.5:
            self.y = (self.y +1) % len(self.environment[0])
        else:
            self.y = (self.y -1) % len(self.environment[0])
    
    
#   Setting the distance between agents & their random movement
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
  
      
#   Communication behavoiural method for agents
#   Where agents can share the elements already 'eaten' with another agent if the distance between the two agents is <5 (neighbourhood)        
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:                   
            distance = self.distance_between(agent) 
            if distance ==0:
                break
            if distance <= neighbourhood:           
                sum = self.store + agent.store      
                avg=sum/2                           
                self.store=avg                      
                agent.store=avg                     
                
      
#   Setting agent consumption 
#   Where the agent can 'eat' 10 elements of the environment if the total number at the location >10               
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10  


#   Agents sicking up consumed stores (using vom function)when their self store exceeds the specified amount
    def vom(self):
        if self.store > 1200:                                   
            self.environment[self.x][self.y] += self.store
            self.store = 500
#   Values set to ensure that the environment will not be completely depleted/consumed
#   Self.store values also set to avoid re-scaling of the map plot
            
            
    
