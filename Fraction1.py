#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:57:00 2018

@author: joykumardas
"""

class Fraction:
    
    def __init__( self, num, deno ):
        self.numerator , self.denominator = Fraction.reduce( num , deno )
        
    @classmethod
    def reduce( cls , top , bottom ):
        common  = cls.gcd( top , bottom )
        return  ( top // common , bottom // common )
    
    @staticmethod
    def gcd( opor , niche ):
        while niche != 0:    
            opor , niche = niche , opor % niche        
            
        return opor
    
    def __str__( self ):
        return str( self.numerator ) + " / " + str( self.denominator )

    def __add__( self , other ):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.numerator
        common = Fraction.gcd( new_numerator , new_denominator )
        return Fraction( new_numerator // common , new_denominator // common )
    
    def __eq__( self , other ):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return new_numerator == new_denominator
    