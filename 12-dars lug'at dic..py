# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:38:26 2021

@author: lenovo
"""

jiyan={"ism":"vali","t_yil":2003,"t_joy":"samarqand"}
tyil=jiyan["t_yil"]
tjoy=jiyan["t_joy"]
name=jiyan["ism"]
print(f"{name.title()}, {tyil}-yilda,{tjoy.title()}da tug'ilgan.")
jiyan={"nom":"ali","t_yil":2003,"t_joy":"samarqand"}
print(f"Bu {jiyan['nom'].title()}, {jiyan['t_yil']}-yil, {jiyan['t_joy'].title()}da tug'ilgan")

dic={
      "olim":"osh",
      "hoshim":"manti",
      "rustam":"lag'mon",
      "komil":"non",
      "lobar":"kabob"
      }
print(f"Olimning sevimli taomi {dic['olim']}")
print(f"Hoshimning sevimli taomi {dic['hoshim']}")
print(f"Rustamning sevimli taomi {dic['rustam']}")
print(f"Komilning sevimli taomi {dic['komil']}")
print(f"Lobarning sevimli taomi {dic['lobar']}")

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
inp=input("Kalit so'z kiriting:").lower()
print(lugat.get(inp, "Bunday so'z mavjud emas."))