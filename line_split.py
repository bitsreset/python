#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:53:53 2018

@author: joykumardas
"""

with open("surfing_data.csv") as fp:
    for line in fp:
        s = {}
        ( s['id'] , s['name'] , s['country'],s['average'],s['board'],s['age'] ) = line.split(';')
        
        print("ID:"+s['id'])
        print("Name"+s['name'])
        print("Country"+s['country'])
        print("Average"+s['average'])
        print("Board Type"+s['board'])
        print("Age"+s['age'])