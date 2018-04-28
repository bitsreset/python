#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:56:34 2018

@author: joykumardas
"""

class Complex:
    
    def __init__( self , real , img = 0.0 ):
        self.real , self.imaginary = real , img 
        
    def __str__( self ):
        return "( {} , {} )".format( str( self.real ) , str( str( self.imaginary ) )) 
    
    def __add__( self, other ):
        new_real = self.real + other.real 
        new_imaginary = self.imaginary + other.imaginary  
        return Complex( new_real , new_imaginary )
    
#c = Complex( 2 , 1 )
