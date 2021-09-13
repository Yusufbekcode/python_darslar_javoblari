# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:56:23 2021

@author: aleyk
"""

def ism_tyil (ism, yosh, now=2021):
    """Foydalanuvchidan ismi va tug'ilgan yilini so'rab,
    yoshini va ismini konsolga chiqaruvchi funksiya"""
    print(f"{ism.title()}, siz {now-yosh} yoshdasiz")
ism=input('Ismingizni kiriting:')
yosh1=int(input("Yoshingizni kiriting:"))
yosh=2021-yosh1
ism_tyil(ism, yosh)

def kv_kub_chiqar(i_raqam):
    """Userdan olingan raqamni kvadrat va
    kubini hisoblaydigan funksiya"""
    print(f"Raqamning kvadrati {i_raqam**2} ga, kubi {i_raqam**3} ga teng") 
i_raqam=float(input("Istalgan raqam kiriting:"))
kv_kub_chiqar(i_raqam)

def toq_juft_aniqla(son):
    """Soning toq yoki juft ekanligini aniqlaydi"""
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")
son=int(input("Raqam kiriting:"))
toq_juft_aniqla(son)        

def kattasini_chiqar(birinchi, ikkinchi):
    if birinchi>ikkinchi:
        print(f"Ikkala sondan eng yirigi {birinchi}")
    elif birinchi<ikkinchi:
        print(f"Ikkala sondan eng yirigi {ikkinchi}")
    else:
        print("Sonlar teng")
kattasini_chiqar(14, 78)  #qavslar ichiga istalgan raqam kiritish mumkin


def kvadrat(x,y):
    """kvadratga oshiradi"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng")
kvadrat(5,5)

def kvadrat(x,y=2):
    """kvadratga oshiradi"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng")
kvadrat(5)

def bolinish_alomatlari(son):
    """"Berilgan raqamni 2 dan 10 gacha bo'lgan raqamlarni qaysi biriga qoldiqsiz 
    bo'linishini aniqlaydi. Qavslar ishiga istalgan butun son kiritishingiz mumkin"""
    raqamlar=list(range(2,11))
    for raqam in raqamlar:
        if not son%rdefaqam:
            print(f"{son} {raqam} ga qoldiqsiz bo'linadi")
bolinish_alomatlari(56)