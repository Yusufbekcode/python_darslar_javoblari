# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:38:33 2021

@author: lenovo
"""

davlatlar=["rossiya", "aqsh", "baa", "turkiya", "angliya", "kanada", "belarus", "shvetsariya"]
print(davlatlar)
print("Davlatlar ro'yxatidagi indekslar soni:", len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
juft_son=list(range(12,1201,2))
print(sum(juft_son))
print(max(juft_son)-min(juft_son))
print("Juft sonlar ro'yxati indekslar soni:", len(juft_son))
bosh20=juft_son[:21]
urta20=juft_son[287:308]
oxiri20=juft_son[-20:]
print(bosh20)
print(urta20)
print(oxiri20)


taomlar=["osh", "kabob", "somsa", "manti", "pizza"]
nonushta=taomlar[:]
del nonushta[1]
nonushta.remove("manti")
nonushta.insert(0, "saryog'li non")
nonushta.append("yong'oq")
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)
print(type(nonushta))