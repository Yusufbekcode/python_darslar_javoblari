# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 21:58:16 2021

@author: aleyk
"""

cars=["toyota", "mazda", "hyundai", "gm", "kia"]
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
        

cars=["toyota", "mazda", "hyundai", "gm", "kia"]
for car in cars:
    if car == "gm":
        print(car.title())
    else:
        print(car.upper())


f_nomi=input("Iltimos loginingizni kiriting:\n>>>")
admin = "Yusufbek"
if f_nomi.lower() == admin.lower():
    print(F"Xush kelibsiz, {admin}. Foydalanuvchilar ro'yxatini ko'rasizmi")
else:
    print("Xush kelibsiz", f_nomi.title())


print("Ixtiyoriy ikkita son kiriting!")
b_son=input("Birinchi raqamni kiriting:")
i_son=input("Ikkinchi raqamni kiriting:")
if b_son==i_son:
    print("Sonlar teng")
if b_son>i_son:
    print("Birinchi son, ikkinchi sondan katta")
if b_son<i_son:
    print("Birinchi son, ikkinchi sondan kichik")

n_son=int(input("Istalgan raqamni kirting:"))
if n_son>0:
    print("Musbat son")
else:
    print("Manfiy son")


sn=float(input("Istagan raqamingizni kiriting:"))
if sn>0:
    print(sn**(1/2))
else:
    print("Musbat son kiriting")

    