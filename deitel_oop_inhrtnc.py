#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:24:55 2018

@author: joykumardas
"""

class Employee:
    """Abstract base class Employe """
    
    def __init__( self, first, last ):
        """Employee constructor,takes first name last name.
        NOTE:Cannot create object of class employee."""
        
        if self.__class__ == Employee :
            raise (NotImplementedError, " Cannot create object of class Employee " )
        
        self.firstName = first
        self.lastName = last
        
    def __str__( self ):
        """String representation of the Employee """
        return "{} {}".format( self.firstName , self.lastName )
    
    def _checkPostive( self , value ):
        """Utility method to ensure a value is positive """
        if value < 0:
            raise ( ValueError , "Attribute value {} must be positive".format( value ))
        else:
            return value
        
    def earnings( self ):
        """Abstract method,derived class must override """
        

        
def main():
    pass

if __name__ == "main":
    main()
