# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:04:47 2022

@author: lenovo
"""

from titlematnfunc import titlematn
import unittest
class Test_titlematn(unittest.TestCase):
    def test_matn(self):
        string=titlematn('matn', 'qiymat', 'olma')
        self.assertEqual(string,['Matn', 'Qiymat', 'Olma'])
unittest.main()
