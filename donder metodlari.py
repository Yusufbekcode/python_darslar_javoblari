# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:01:20 2022

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
    def get_fanlar(self):
        while True:
            for fan in self.fanlar:
                print(fan)
            else:
                break
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def __getitem__(self, index):
        return self.fanlar[index]
    def __call__(self):
        m=f"Talaba, {self.ism} {self.familiya} yozilgan fanlar:\n"
        m+=self.get_fanlar()
        print(m)
    
talaba=Talaba("Malik","Abrorov","AB36469556", 2000, 647648565)   
g=talaba.fanga_yozil("Geometriya")
ch=talaba.fanga_yozil("Chizmachilik")
jt=talaba.fanga_yozil("Jismoniy Tarbiya")
# print(talaba.get_fanlar())