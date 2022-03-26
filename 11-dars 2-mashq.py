# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 08:44:39 2021

@author: lenovo
"""

yosh=int(input("Yoshingizni kiriting:"))
if yosh<4 or yosh>60:
    narx=0
elif yosh<18:
    narx=10000
else:
    narx=20000
print(f"Siz uchun chipta narxi {narx} so'm")