#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:49:45 2018

@author: joykumardas
"""

class Fraction:
    
    def __init__( self , top , bottom ):
        self.numerator , self.denominator = Fraction.reduce( top , bottom )
        
    @classmethod
    def reduce( cls , numrtr , dnmntr ):
        common = cls.gcd( numrtr , dnmntr )
        return ( numrtr // common , dnmntr // common )
    
    @staticmethod 
    def gcd( numerator , denominator ):
            while denominator != 0 :
                numerator , denominator = denominator , numerator % denominator
            
            return numerator
        
    def __str__( self ):
        return str( self.numerator ) + " / " + str( self.denominator )
    
x = Fraction( 8 , 24 )
print(x)