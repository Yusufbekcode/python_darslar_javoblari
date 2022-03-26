# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:10:52 2022

@author: lenovo
"""
import pickle
with open('pi_million_digits.txt') as files:
    pison=files.read()
pison=pison.rstrip()
pison=pison.replace("\n","")
pison=pison.replace(' ','')
tsana="01062001"
print(tsana in pison)
pison=float(pison)
with open('pi_son.pickle', 'wb') as file:
    pickle.dump(pison,file)
    