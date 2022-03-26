# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:40:55 2022

@author: lenovo
"""

import unittest
from circle import getArea, getPerimetr

class Circletest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5),78.53975,3)
        self.assertAlmostEqual(getArea(12),452.38896)
        
    def test_perimetr(self):
        self.assertAlmostEqual(getPerimetr(5),31.4159)
        self.assertAlmostEqual(getPerimetr(50),314.159)
        
unittest.main()
        