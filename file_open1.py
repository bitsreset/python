#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 00:28:36 2018

@author: joykumardas
file_open1.py
"""
#file_name = "results.txt"
file_name = "results_name.txt"
with open( file_name ) as fp:
    #for cnt, line in enumerate(fp):
    highest_score = 0.0
    for line in fp:
        name , score = line.split()
        this_score = float(score)
        if this_score  > highest_score:
            highest_score = this_score
            this_name = name
            
    print(this_name,highest_score)
        #print("{0} {1}".format( cnt , line ))

