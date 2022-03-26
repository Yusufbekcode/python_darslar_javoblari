# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:06:00 2022

@author: lenovo
"""

def name(ism, familya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familya}".title()
    else:
        return f"{ism} {familya}".title()