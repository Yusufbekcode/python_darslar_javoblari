# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:11:18 2022

@author: lenovo
"""

import unittest
from namefunc import name

class Testname(unittest.TestCase):
    def test_names(self):
        nam=name('ali','numonov')
        self.assertEqual(nam, 'Ali Numonov')
    def test__otasi(self):
        nam=name('ali', 'numonov', 'azizovich')
        self.assertEqual(nam, 'Ali Azizovich Numonov')
        
unittest.main()