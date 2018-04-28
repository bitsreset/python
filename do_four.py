#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:00:39 2017

@author: joykumardas
do_four.py
"""

def do_four(f,val):
    f(val)
    f(val)

def print_string(s):
    print(s)
    print(s)

do_four(print_string,'spam')