# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:57:59 2022

@author: lenovo
"""

def titlematn(*matn):
    """Kiritilgan matnni birinchi harflarini bosh harfga o'zgartiradi"""

    r=[m.title() for m in matn]
    return r