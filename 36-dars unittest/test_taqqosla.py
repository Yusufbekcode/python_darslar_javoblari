# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:37:05 2022

@author: lenovo
"""

from xyz_taqqoslafunc import *
import unittest
class Test_taqqosla(unittest.TestCase):
    def test_taqq(self):
        taqq=taqqosla(6, 9, 3)
        self.assertEqual(taqq, '6<9>3')
unittest.main()