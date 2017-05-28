#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:32:10 2017
random_uppercase.py
@author: joykumardas
(Random character) Write a program that displays a random uppercase letter
using the time.time() function.
"""

import time

currentTime = time.time()
totalSeconds = int(currentTime)
noOfChars=26
asciiSecond = totalSeconds % noOfChars
print("The upper case character is:",chr(asciiSecond+65))
