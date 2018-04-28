#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:17:58 2018

@author: joykumardas
"""

class A:
    
    def __init__( self , i ):
        self.i = i 
        
    def __str__( self ):
        return "A"
    
    def __eq__( self , other ):
        return self.i == other.i

x = A( 1 )
y=  A( 1.0 )

print( x == y )