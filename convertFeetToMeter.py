# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:24:18 2017

convertFeetToMeter.py

@author: joydas
(Convert feet into meters) Write a program that reads a number in feet,
converts it to meters, and displays the result. 
One foot is 0.305 meters. 
Here is a sample run:
Enter a value for feet:16.5 
16.5 feet is 5.0325 meters
"""
feet = eval(input("Enter a value for feet:"))
meters = feet * 0.305
print(feet, "feet is ",meters,"meters")
