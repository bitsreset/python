#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 16:01:30 2017

@author: joykumardas
conditional_start.py
"""

def main():
    print("Hello")
    x,y = 100,1000
    print("x=",x,"\ny=",y)
    if x < y:
        st ="x is less than y"
    elif x == y:
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print(st)
    
    print("ternary operator usage::")
    new_st= "x is less than y" if x < y else "x is greater or equal to y"
    print(new_st)
    
if __name__ == "__main__":
    main()
