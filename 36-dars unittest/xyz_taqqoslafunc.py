# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:21:49 2022

@author: lenovo
"""

def taqqosla(x,y,z):
    if z<x>y:
        return f"{z}<{x}>{y}"
    elif x<z>y:
        return f"{x}<{z}>{y}"
    else:
        return f"{x}<{y}>{z}"
    