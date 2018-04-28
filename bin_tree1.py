#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:21:06 2018

@author: joykumardas
"""

class Node:
    def __init__( self , data ) :
        self.left = None
        self.right = None
        self.root = data
    
    def inOrder( cls  ):
        if self.root:
            inOrder( self.root.left )
            print( self.root.data )
            inOrder( self.root.right )
        
        
#making the tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root.inOrder())