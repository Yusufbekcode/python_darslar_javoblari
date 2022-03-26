# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:22:04 2021

@author: lenovo
"""

mahsulotlar=["uzum", "olma", "qozon", "changyutgich", "tova", "banan", "archa", "murabbo", "futbolka", "kostyum", "paypoq", "tort"]
bor=[]
yuq=[]
savat=[]
for mahsulot in range(5):
    savat.append(input(f"{mahsulot+1}-mahsulot nomini kiriting:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor.append(mahsulot)
    if mahsulot not in mahsulotlar:
        yuq.append(mahsulot)
if yuq:
    print("Do'konimizda quyidagi mahsulotlar yuq:")
    for mahsulot in yuq:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar bizda bor.")