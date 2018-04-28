#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 09:23:33 2018

@author: joykumardas
program.py
"""

def main():
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we cant search that location.")
        return
    
    text = get_search_text_from_user()
    if not text:
        print("we can't search for nothing.")
        return
    
    search_folders( folder , text )

def print_header():
    print('-----------------------------------')
    print(' File Search App                   ')
    print('-----------------------------------')

def get_folder_from_user():
    pass

def get_search_text_from_user():
    pass

def search_folders ( folder , text ):
    pass






if __name__ == '__main__':
    main()