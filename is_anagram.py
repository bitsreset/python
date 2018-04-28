#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:37:08 2018

@author: joykumardas
Write a function to check if two strings are anagrams

string1: "1bcadd"
string2: "dadcb1"

return value: true
"""
def is_anagram( word1 , word2 ):
    return sorted( word1 ) == sorted( word2)

print(is_anagram("1bcadd" , "dadcb1") )