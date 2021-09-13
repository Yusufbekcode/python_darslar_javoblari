# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:09:12 2021

@author: aleyk
"""

buyurtma_mahsulot=[]
while True:
    mahsulot=input("Buyurtma mahsulotlaringizni kiriting:\n>>>")
    buyurtma_mahsulot.append(mahsulot)
    qaror=input('Yana biror nima kiritishni xohlaysizmi?(ha,yoq)')
    if qaror=='yoq':
        break
    
    
e_bozor={}
flag=True
while flag:
    mah_nom=input("Mahsulot nomini kiritting:")
    mah_narx=input(f"{mah_nom.title()} narxini kiriting:")
    e_bozor[mah_nom]=int(mah_narx)
    
    
    qaror1=input("Yana ma'lumot kiritishni xohlaysizmi? ('ha', 'yoq')")
    if qaror1=='yoq':
        flag=False
    
for mahsulot in buyurtma_mahsulot:
    if mahsulot in e_bozor.keys():
        print(f"{mahsulot.title()} {mah_narx}so'm")
    else:
        print(f"Bizda {mahsulot} yo'q")
            