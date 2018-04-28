#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 08:00:47 2018
test_interview_function.py
@author: joykumardas
"""

import unittest
from interview_functions import function1

class TestFunction1( unittest.TestCase ):
    
    def test_function1( self ):
        expected = [0,0,1,0,1,2 ]
        actual = function1(3)
        #print(actual)
        
        self.assertEqual( expected , actual )
        

if __name__ == '__main__' :
    unittest.main()