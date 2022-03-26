# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:00:42 2022

@author: lenovo
"""


class Talaba:
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar=[]
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    def fanga_yozil(self,fans):
        self.fanlar.append(fans)
        return self.fanlar
    def remove_fan(self,fan):
        for fan in self.fanlar:
            if fan in self.fanlar:
                self.fanlar.remove(fan)
            else:
                print("Siz bu fanga yozilmagansiz.")
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
class Fan:
    def __init__(self,fan):
        self.fan=fan

    
talaba=Talaba("Malik","Abrorov","AB36469556", 2000, 647648565)
g=Fan("Geometriya")
onaTili=Fan("Ona tili")
ch=Fan("Chizmachilik")
talaba.fanga_yozil(g)
talaba.fanga_yozil(ch)
talaba.remove_fan(onaTili)