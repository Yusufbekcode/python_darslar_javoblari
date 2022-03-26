# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:24:15 2022

@author: lenovo
"""

from uuid import uuid4
class Talaba:
    """Talaba klassi"""
    __talabalar_soni=0
    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        self.__idraqam = uuid4()
        self.__bosqich =1
        Talaba.__talabalar_soni+=1
        self.fanlar=[]
    def get_id(self):
        """Talabaning ID raqami"""
        return self.__idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.__bosqich
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
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.__idraqam}"
        return info
    def set_bosqich(self):
        self.__bosqich+=1
        
    @classmethod
    def get_talabaSoni(cls):
        return cls.__talabalar_soni
talaba=Talaba('Aziz', 'Davronov', 'AB4563289', 2000)
print(talaba.get_info())


