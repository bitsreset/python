#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:30:32 2018

@author: joykumardas
"""

class Robot:
    
    __counter = 0 
    
    def __init__( self  ):
        type( self ).__counter += 1
        
    @staticmethod
    def RobotInstance():
        return Robot.__counter
    
print(Robot.RobotInstance())
x = Robot()
print(x.RobotInstance())
y = Robot()
print(y.RobotInstance())
print(Robot.RobotInstance())