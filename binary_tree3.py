#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 04:15:53 2018

@author: joykumardas
"""

class Node:
    def __init__( self , data = None ):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    
    def __init__( self ):
        self.root_node = None
        
#    def __str__( self ):
#        return self.

    def insert( self , data ):
        node = Node( data )
        
        if self.root_node == None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                
                if node.data < current.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return
                    
                
        