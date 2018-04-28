#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:39:59 2018

@author: joykumardas
"""

class Pets:
    name = "pet animals"
    
    @staticmethod
    def about():
        print( "This class is about " + Pets.name )
    
class Dogs( Pets ):
    name = "Mans best friends"
    
class Cats( Pets ):
    name = "Cats"
    
p = Pets()
print(p.about())

d = Dogs()
print(d.about())

c = Cats()
print(c.about())
    