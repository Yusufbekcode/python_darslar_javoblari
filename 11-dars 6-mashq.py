# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:38:46 2021

@author: lenovo
"""

users=["halim", "olim", "wolf", "yusuf", "qwerty"]
user=(input("Yangi login tanlang:"))
if user.lower() in users:
    print("Bu login band. Bohqa login tanlang!!!")
else:
    print(f"Xush kelibsiz {user.title()}")
    