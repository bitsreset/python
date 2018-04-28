#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:37:09 2018

      1
   2    3
 4   5 6  7
 
 Output: 4251637

@author: joykumardas
"""

class Node:
    """
    Tree Node: left and right child + data which can be any object
    """
    
    def __init__( self, data ):
        self.left = None
        self.right = None
        self.data = data
        
    def insert( self, data ):
        
        if self.data:
            "insertion in left node"
            if data < self.data:
                if self.left is None:
                    self.left = Node( data )
                else:
                    self.left.insert( data )
                    
            #insertion in right node
            elif data > self.data:
                if self.right is None:
                    self.right = Node( data )
                else:
                    self.right.insert( data )
        else:
            self.data = data
            
    def print_tree( self ):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()
