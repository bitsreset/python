#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:25:07 2018

@author: joykumardas
pallindrome.py
A palindrome is  a number or a text phrase that reads the same backwards or 
forwards,For example,each of following five-digit integers is a palindrome:
12321,55555,45554 and 1234.Write a program that reads in a five-digit integer and detremines whether it is a 
palindrome.(Hint:Use the division and modulus  operator to separate the number
into its individual digits.)
"""

#def main():
#    number = int(input("Enter any number :: "))
#    #print("Number entered ? ",number)
#    
#    if is_palindrome( number ) == number:
#        print(f"{number} is palindrome")
#    else:
#        print(f"{number} is not palindrome")

def is_palindrome( number ):
    reverse_num = 0 
    while( number ):
        remainder = number % 10
        #print("remainder",remainder)
        number = number // 10 
        #print("number",number)
        reverse_num = reverse_num * 10 + remainder 
    
    #print(org_number,reverse_num)
    return reverse_num

#if __name__ == '__main__':
#    main()

