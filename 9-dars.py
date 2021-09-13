# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 11:26:29 2021

@author: aleyk
"""

ismlar=["Shaxzod", "Olim", "G'ayrat", "Temur", "Ziyovuddin"]
for ism in ismlar:
    print(ism, "bugun python bo'icha maruza bo'ladi.")
print("Kod", len(ismlar), "marta takrorlandi")    
toq_sonlar=list(range(11,100,2))
toq_sonlar_kubi=[]
for son in toq_sonlar:
    toq_sonlar_kubi.append(son**3)
print(toq_sonlar_kubi)
for soni in toq_sonlar:
    print(soni**3)
sev_kinolar=[]
print("5 ta eng yoqtirgan kinoyingiz nomini yozing")
for sev_kino in range(5):
    sev_kinolar.append(input(f"{sev_kino+1}- kinoni nomini kiriting:\n>>>"))
print(sev_kinolar)
x_sonlar=int(input("Bugun nechta odam bilan suhat qildingiz;\n>>>"))
suhbatdoshlar=[]
for x_ism in range(x_sonlar):
    suhbatdoshlar.append(input(f"{x_ism+1} - suhbatdoshingiz ismini kiriting:\n>>>"))
print(suhbatdoshlar)