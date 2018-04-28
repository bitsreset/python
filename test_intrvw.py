#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:52:27 2018

@author: joykumardas
"""

def compute(): 
    d = {} 
    for c in (65, 97): # 'A' and 'a' 
        for i in range(26): 
            d[chr(i+c)] = chr((i+13) % 26 + c) 
    return d 

d = compute()

print(d)
s = "Hello Encryption" 
print("Encrypted:", "".join([d.get(c, c) for c in s]) )

s = "Hello Encryption" 
print("Encrypted:", "".join([d[c] for c in s]))