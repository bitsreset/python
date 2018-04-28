#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:54:01 2018

@author: joykumardas
"""

from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


    def add(node, root):
        if root is None:
            raise ValueError('root cannot be None.')
    
        nodes_found = deque([root])
        print("{0} = deque({1})".format(nodes_found,root))
    
        while len(nodes_found) > 0:
            current_node = nodes_found.popleft()
            print("{0}".format( current_node ))
    
            if current_node.left is None:
                current_node.left = node
                print("current_node.left = node:: {0} = {1}".format(current_node.left,node))
                break
            if current_node.right is None:
                current_node.right = node
                print("current_node.right = node:: {0} = {1}".format(current_node.right,node))
                break

        nodes_found.append(current_node.left)
        nodes_found.append(current_node.right)
        
root = Node(8)
keys = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

for key in keys:
    add(Node(key), root)