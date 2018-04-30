#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 19:34:29 2018

@author: joykumardas
"""

import unittest
import pallindrome

class TestPallindrome( unittest.TestCase ):
    
    def test_pallindrome( self ):
        original = 12321
        expected = pallindrome.is_palindrome( original )
        self.assertEqual( original , expected )
    
if __name__ == '__main__':
    unittest.main()