# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:13:59 2017

@author: joydas
(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from
the console and converts it to Fahrenheit and displays the result. The formula for
the conversion is as follows:
fahrenheit = (9 / 5) * celsius + 32

Here is a sample run of the program:
Enter a degree in Celsius: 43
 Celsius is 109.4 Fahrenheit
"""

celsius = eval(input("Enter a degree in Celsius:"))
fahrenheit = (9 / 5) * celsius + 32
print("Celsius is",fahrenheit,"Fahrenheit")
