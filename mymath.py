#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:43:53 2018

@author: joykumardas
"""

"""mymath - our example math module """
pi = 3.14159
def area( r ):
    """area( r ): return the area of a circle with radius r. """
        global pi
    return ( pi * r * r )