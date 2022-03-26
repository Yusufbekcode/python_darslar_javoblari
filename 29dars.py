# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:43:13 2022

@author: lenovo
"""

class Avto:
    def __init__(self, model, rang, karobka, narh, myear):
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.cost=narh
        self.year=myear
        self.masofa=0
        self.texpasport=None
    def get_info(self):
        return f"""Avtomobil ma'lumotlari:
            Modeli-{self.model}
            Rangi-{self.rang}
            Karobka-{self.karobka}
            Narh-{self.cost}
            Ishlab chiqarilgan yili-{self.year}
            Bosgan masofasi[km]-{self.masofa}
            Texpasport-{self.texpasport}"""
            
    def update_km(self,km):
        self.masofa+=km
    def update_cost(self,cost):
        self.cost+=cost
    def tex(self,f):
        self.texpasport=f
avto1=Avto('Nexia3', 'qora', 'avtomat', 16000, 2021)
avto1.tex('bor')
avto1.update_km(10000)
avto1.update_cost(200)
# print(avto1.get_info())
avto2=Avto('Mustang', 'qora', 'mexanik', 25000, 2005)
avto2.update_km(260000)
avto2.tex('mavjud')
# print(avto2.get_info())

class Avtosalon:
    def __init__(self,nomi, manzil, tel):
        self.nomi=nomi
        self.manzil=manzil
        self.tel=tel
        self.avtolar=[]
    def add_avto(self,avto):
        self.avtolar.append(avto)
        
    def get_avtolar(self):
        return [avtos.get_info() for avtos in self.avtolar]
salon=Avtosalon('Nur', 'Samarqand sh.', '+998663215645')
salon.add_avto(avto2)
salon.add_avto(avto1)
print(salon.get_avtolar())