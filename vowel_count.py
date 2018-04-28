#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 23:56:33 2018

@author: joykumardas
"""

s = 'azcbobobegghakl'
vowel_count = 0
for each_ch in s:
    if each_ch in 'aeiou':
        vowel_count += 1
        
print("Number of vowels: {}".format( vowel_count ))