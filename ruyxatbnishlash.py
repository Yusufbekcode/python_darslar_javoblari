# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:24:42 2021

@author: aleyk
"""

py3_lugat={
    'integer':'Butun son',
    'float':'O\'nlik son',
    'string':'Matn',
    'boolean':'mantiqiy qiymat',
    'for':'Biror amalni qayta qayta bajarish tsikli',
    'dictionary':'Lug\'at',
    'list':'Ro\'yxat',
    'if':'shartlarni tekshirish operatori'
    }
for k, q in sorted(py3_lugat.items()):
    print(f"{k.title()} - {q}")

dav_poy={
    'aqsh':'vashington',
    'italiya':'rim',
    'rossiya':'moskva',
    'ispaniya':'madrid',
    'angliya':'london',
    'fransiya':'parij',
    'o\'bekiston':'toshkent',
    'germaniya':'berlin'}
print("Dunyo davlatlari:")
for dav in sorted(dav_poy):
    print(dav.upper())
print('\nDavlatlarning poytaxtlari:')
for poy in sorted(dav_poy.values()):
    print(poy.title())

foy_dav=input('Qaysi davlatni poytaxtini bilishni xohlaysiz?\n>>>')
if foy_dav.lower() in dav_poy:
    print(f"{foy_dav.upper()} poytaxti ")



