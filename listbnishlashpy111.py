# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:18:13 2021

@author: aleyk
"""
davlatlar=["Qozog'iston", "Ukraina", "Afrika", "Turkiya"]
print(davlatlar)
len(davlatlar)
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
j_sonlar=list(range(120,1200,2))
print(j_sonlar)
print(sum(j_sonlar))
kichik=min(j_sonlar)
katta=max(j_sonlar)
print(katta-kichik)
print(j_sonlar[0:21])
print(j_sonlar[260:281])
print(j_sonlar[520:])
taomlar=["Osh", "Kabob", "Makaron", "Sho'rva", "Somsa"]
nonushta=taomlar[:]
nonushta.remove("Makaron")
del nonushta[2]
nonushta.insert(0, "Saryog'")
nonushta.append("Sut")
print(taomlar)
print(nonushta)
nonushta=tuple(nonushta)
#nonushta.append("Baliq") attributeerror. sababi bu list tuple
