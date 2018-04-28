#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:06:36 2018

Write a function that finds the first non repeated character in a string

@author: joykumardas
"""
myString = "llo World"
my_list = list(myString)
index = 0
len_my_list = len( my_list ) 
print("len( my_list ) = " , len_my_list )
while index < len_my_list :
    print('current index = ' , index )
    cur_char = my_list[ index ]
    print('cur_char = ' , cur_char )
    
    if index <=  len_my_list - 2 and cur_char.isalnum() :
        if cur_char in my_list[ index + 1 : ]:
            pass
        else:
            print(cur_char,"First non-repeated")
            break
    else:
        print("String iteration ended")
    
    index += 1