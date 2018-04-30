# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:44:03 2017

tipsCalculator.py

@author: joydas
(Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total. Here is a sample run:
Enter the subtotal and a gratuity rate: 15.69, 15
The gratuity is 2.35 and the total is 18.04
"""
subtotal , gratuity_rate = eval(input("Enter the subtotal and a gratuity rate:"))
print("The subtotal is ",subtotal,"and the gratuity_rate is ",gratuity_rate)
gratuity = ( gratuity_rate  * subtotal ) / 100
total = subtotal + gratuity
print("The gratuity is ",gratuity,"and the total is",total)
