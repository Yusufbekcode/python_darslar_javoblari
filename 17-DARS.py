# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:24:18 2021

@author: aleyk
"""

kitob = "Yoqtirgan kitoblaringizni kiriting "
kitob +="(Dasturni to'xtatish uchun 'stop' deb yozing):"
while True:
    qiymat=input(kitob)
    if qiymat == 'exit':
        break 
print("Rahmat")


yosh="Yoshingizni kiriting: "
while True:
    qiymat=input(yosh)
    if qiymat == 'exit' or qiymat== 'quit':
        break
    yosh1=int(qiymat)
    if yosh1<7:
        print("Chipta narxi 2000 so'm.")
    elif yosh1<18:
        print("Chipta narxi 3000 so'm.")
    elif yosh1<65:
        print("Chipta narxi 10000 so'm.")
    else:
        print("Chipta siz uchun bepul.")

yosh="Yoshingizni kiriting: "
flag= True
while flag:
    qiymat=input(yosh)
    if qiymat == 'exit' or qiymat== 'quit':
        flag= False 
    else:
        yosh1=int(qiymat)
        if yosh1<7:
            print("Chipta narxi 2000 so'm.")
        elif yosh1<18:
            print("Chipta narxi 3000 so'm.")
        elif yosh1<65:
            print("Chipta narxi 10000 so'm.")
        else:
            print("Chipta siz uchun bepul.")





    