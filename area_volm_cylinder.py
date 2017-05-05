# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:18:26 2017
area_volm_cylinder.py
@author: joydas
(Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * π
volume = area * length
Here is a sample run:
Enter the radius and length of a cylinder:5.5, 12
The area is 95.0331
The volume is 1140.4
"""

radius , length_of_cylinder = eval(input("Enter the radius and length of a cylinder:"))
area_of_cylinder = radius * radius * 3.14159
volume_of_cylinder = area_of_cylinder * length_of_cylinder
print("The area is ",area_of_cylinder)
print("The volume is ",volume_of_cylinder)
