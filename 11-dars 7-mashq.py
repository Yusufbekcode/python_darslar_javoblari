# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:49:32 2021

@author: lenovo
"""

xson=int(input("Istalgan butun son kiriting."))
for n in range(2,11):
    if not (xson%n):
        print(f"{xson} soni {n} ga qoldiqsiz bo'linadi.")