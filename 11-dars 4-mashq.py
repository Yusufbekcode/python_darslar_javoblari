# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:03:17 2021

@author: lenovo
"""

mahsulotlar=["uzum", "olma", "qozon", "changyutgich", "tova", "banan", "archa", "murabbo", "futbolka", "kostyum", "paypoq", "tort"]
savat=[]
for mahsulot in range(5):
    savat.append(input(f"{mahsulot+1}-mahsulot nomini kiriting:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Bizda {mahsulot} bor")
    if mahsulot not in mahsulotlar:
        print(f"Bizda {mahsulot} yuq")
    
    