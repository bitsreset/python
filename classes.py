#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 08:26:45 2018
classes.py
@author: joykumardas
"""
class MyClass(object):
    def __init__( self , x , y ):
        self.x = x
        self.y = y
        print('inside __init__:',self)

my_object = MyClass(1,2)
print(my_object.x,my_object.y)