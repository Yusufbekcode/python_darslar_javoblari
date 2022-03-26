# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 09:23:30 2021

@author: lenovo
"""

lugat={
        "int":"butun son",
        "float":"o'nlik son",
        "string":"matn",
        "loop":"for tsikli",
        "dictionary":"lug'at",
        "if":"agar deb tarjima qilinadi",
        "else":"bir nechta amalni tekshiradi",
        "list":"ro'yxat",
        "tuple":"o'zgarmas ro'yxat"
        }
for k, v in sorted(lugat.items()):
    print(f"{k.title()}-{v.capitalize()}")
    
cap_count={
    "usa":"washington",
    "russia":"moskov",
    "uzbekistan":"tashkent",
    "kazakhstan":"astana",
    "england":"london",
    "italiya":"rim"
    }
print("Dunyo davlatlari:")
for dav in sorted(cap_count):
    print(dav.upper())
print("Davlatlarning poytaxtlari:")
for poy in sorted(cap_count.values()):
    print(poy.title())
country=input("Qaysi davlatni poytaxtini bilishni xohlaysiz?\n>>>").lower()
k=cap_count.get(country)
if k==None:
    print("Bizda bunday ma'lumot yuq.")
else:
    print(f"{country.upper()}ning poytaxti {k.title()} shahri.")
    
    
menu={
      "osh":20000,
      "non":3000,
      "choy":1000,
      "kabob":15000,
      "lag'mon":13000,
      "jiz":15000,
      "limon choy":3000,
      "manti":5000,
      "somsa":6000
      }
print("Marhamat  3 ta taom buyurtma qilishingz mumkin!")
buyurtmalar=[]
for b in range(3):
    buyurtmalar.append(input(f"{b+1}-taomga nima buyurtma qilasiz?\n>>>").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")