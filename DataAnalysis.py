#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:05:02 2017

@author: joykumardas
DataAnalysis.py

"""

NUMBER_OF_ELEMENTS=5
numbers=[]
sum=0

for i in range(NUMBER_OF_ELEMENTS):
    value = int(input("Enter a new number"))
    numbers.append(value)
    sum += value
    
average = sum / NUMBER_OF_ELEMENTS

count = 0
for i in range(NUMBER_OF_ELEMENTS):
    if numbers[i] > average:
        count += 1
    
print("Average is",average)
print("Number of elements above the average is",count)