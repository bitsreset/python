#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:49:38 2017

@author: joykumardas
function_object1.py
"""
def do_twice(f,val):
    f(val)
    f(val)
    
def print_spam(s):
    print(s)

do_twice(print_spam,'spam')