# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 19:31:02 2022

@author: lenovo
"""
e_bozor={}
print("Mahsulot va uning narxlarini kiritishingiz mumkin.")
metka=True
while metka:
    mahsulot=input("Mahsulot kiriting:").lower()
    narx=input(f"{mahsulot.title()}ning narxini kiriting:")
    e_bozor[mahsulot]=int(narx)
    surov=input("Kiritishni yakunlaysizmi?\n['ha'||'yoq']").lower()
    if surov=='yoq':
        metka=False

buyurtmalar=[]
print("Buyurtma qilmoqchi bo'lgan mahsulotlaringizni kiriting:")
while True:
    buyurtma=input("Mahsulot kiriting:\n>>>").lower()
    buyurtmalar.append(buyurtma)
    savol=input("Davom etasizmi?").lower()
    if savol=='yoq' or savol=='yuq' or savol=='yo\'q' :
        break
    

for buyurtma in buyurtmalar:
    if buyurtma in e_bozor:
        print(f"{buyurtma.title()}ning narxi {e_bozor[buyurtma]} so'm")
    else:
        print(f"Bizda {buyurtma.title()} yo'q")


