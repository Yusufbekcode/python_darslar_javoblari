# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 19:12:40 2022

@author: lenovo
"""

def user_info(ism, familya, t_joy, t_yil, tel_raqam, yosh, email='' ):
    """Foydalanuvchidan shaxsiy ma'lumotlarni yig'adi"""
    user={"ismi":ism,
        "familyasi":familya,
        "t_joy":t_joy,
        "t_yil":t_yil,
        "yoshi":yosh,
        "tel_raqam":tel_raqam,
        "email":email}
    return user
users=[]
while True:
    print("Quyidagi ruyxatni to'ldiring!",end='')
    familya=input("Familyangiz:")
    ism=input("Ismingiz:")
    t_joy=input("Tug'ilgan manzilingiz(viloyat):")
    t_yil=int(input("Tug'ilgan yilingiz:"))
    tel_raqam=input("Telefon raqamingiz:")
    yosh=2021-t_yil
    email=input("Elektron pochta manzilingiz(ixtiyoriy):")
    users.append(user_info(ism, familya, t_joy, t_yil, yosh, tel_raqam, email))
    surov=input("Yana ma'lumot kiritishni xohlaysizmi[ha,yoq]?")
    if surov=="yoq":
        break