# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:20:27 2022

@author: lenovo
"""

import json
# topshiriq='PI\\students.json'
# with open(topshiriq) as st:
#     sts=json.load(st)
    


# for item in sts["student"]:
#     print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")
    

tpq5='PI\\apiresult.json'
with open(tpq5) as api:
    ap=json.load(api)
title=ap['query']['pages']['13801']['title']
extract=ap['query']['pages']['13801']['extract']