# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:56:22 2022

@author: lenovo
"""
import json
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_jsn=json.dumps(data)
print(type(data))
print(data_jsn)
print(type(data_jsn))
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
talaba=json.loads(talaba_json)
print(f"Talaba, {talaba['ism']} {talaba['familiya']}")

filename='json_darsi_data.dic'
with open(filename, 'w') as y:
    y.write(data_jsn)
fname='json_darsi_talaba.dic'
with open(fname, 'w') as d:
    d.write(talaba_json)
    