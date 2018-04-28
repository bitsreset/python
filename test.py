#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:47:03 2018

@author: joykumardas
"""

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print(fib(5))