# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 19:25:10 2022

@author: lenovo
"""

def userinfocollect(ism, born, now=2022):
    """"Foydalanuvchidan ismi va tug'ilgan yilini chiqarib beradi"""
    print(f"{ism.title()} siz {now-born} yoshdasiz")
name=input("Ismingizni kiriting:")
old=int(input("Tug'ilgan yilingizni kiriting:"))
userinfocollect(name, old)


def kub_kv(number):
    """Bu funksiyaga istalgan son kiritib uning kvadrati
    va kubini bilib olishingiz mumkin."""
    print(f"{number} ning kvadrati {number**2}")
    print(f"{number} ning kubi {number**3}")
kub_kv(5)


def juft_toq_aniqla(x):
    """Sonni juft yoki toq ekanligini aniqlaymiz."""
    if x%2==0:
        print(f"{x} soni juft son.")
    else:
        print(f"{x} soni toq son.")
number=int(input("Berilgan sonni toq yoki juft ekanligini aniqlaymiz.\nMarhamat butun son kiriting:"))
juft_toq_aniqla(number)


def taqqosla(r, t):
    """Ikkita berilgan raqamlarni taqqoslaydi.
    Va kattasini konsolga chiqaradi.
    Agar sonlar teng bo'lsa 'Sonlar teng' matnini chiqoradi."""
    if r>t:
        print(f"{r} katta {t} dan {r}>{t}")
    elif r==t:
        print(f"Sonlar teng {r}={t}")
    else: print(f"{t} soni {r} dan katta {t}>{r}")
print("Marhamat yangi taqqoslovchi  'taqqosla()' funksiyamizni sinab ko'ring")
        

def daraja_oshir(x,y):
    """Birinchi x sonini ikkinchi y songa daraja ko'taradi."""
    print(f"{x}ning {y}-darajasi {x**y} ga teng")
daraja_oshir(6, 2)#misol uchun kiritildi!!!

def daraja_oshir(x,y=2):
    """Birinchi x sonini ikkinchi y songa daraja ko'taradi."""
    print(f"{x}ning {y}-darajasi {x**y} ga teng")
daraja_oshir(6, 2)#misol uchun kiritildi!!!

def bolinish_alomatlari(n):
    """Berilgan sonni 2dan 10 gacha bo'lgan sonlar ichida 
    qoldiqsiz bo'linadiganlarini aniqlaydi"""
    for m in range(2,11):
        if not n%m:
            print(f"{n}  {m} ga qoldiqsiz bo'linadi.")
bolinish_alomatlari(60)