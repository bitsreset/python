#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 20:24:23 2018

@author: joykumardas
"""
import sys

counts = {}

for line in sys.stdin:
    words = line.split()
    for word in words:
        counts[ word ] = counts.get( word , 0 ) + 1

print( counts )