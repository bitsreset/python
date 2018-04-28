#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 07:58:21 2018
interview_functions
@author: joykumardas
"""
#def function1( n ):
#    result = []
#    for i in range( 1, n ):
#        if i % 3 == 0:  
#            result.append( i )
#        
#    return result

#def function1( n ):
#    return [ i  for i in range(1,n) if i % 3 == 0 ]

#def function1(n):
#    result = []
#    
#    for i in range(n):
#        for j in range(i+1):
#            result.append(j)
#            
#    return result
def function1( n ):
    return [ j for i in range(n) for j in range(i+1)]