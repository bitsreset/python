#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 23:17:52 2017

@author: joykumardas
for_loop1.py
"""

def main():
    for i in range(5,10):
        #if i == 7:break
        if i % 2 == 0:continue
        print(i)
    
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    for d in enumerate(days):
        print(d)
        
if __name__ == '__main__':
    main()