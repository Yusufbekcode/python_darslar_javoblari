# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:06:32 2021

@author: lenovo
"""

ismlar=["abdulloh", "a'zam", "shaxzod"]
print(f"Salom {ismlar[0].title()} ertaga futbolga borasanmi?")
print(f"{ismlar[1].title()} dam olish kuning hashar qilamiz.")
print(f"{ismlar[-1]} ko'rinmay ketting, nimalar bilan bandsan?")


sonlar=[]
sonlar.append(135)
sonlar.append(-855)
sonlar.append(0.26)
sonlar.append(52)
sonlar.append(8.32)
print(sonlar)
sonlar[2]=sonlar[2]*5
sonlar.insert(1, -55)
del sonlar[-2]
sonlar.remove(135)
sonlar.append(364)


dust1=ismlar.pop(0)
dust2=ismlar.pop(1)
dust3=ismlar.pop(-1)
print(f"{dust1.title()} nega kelmading futbolga?\n Zo'r o'yin bo'ldi.")
