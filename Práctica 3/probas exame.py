# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:25:14 2022

@author: uxiom
"""
from array_positional_list import ArrayPositionalList 

Pl = ArrayPositionalList()
p = 10
for N in range(10) :   
    Pl.add_last(p)
    p += 10
    
def funcion(Pl, n):
    Pl1 = ArrayPositionalList()
    assert n < len(Pl)
    marker = Pl.first()
    mod = len(Pl) // n
    for item in range(n-1):
        marker = Pl.after(marker)
    Pl1.add_first(Pl.get_element(marker))
    for i in range(mod-1):
           for x in range(n):
               marker = Pl.after(marker)
           Pl1.add_last(Pl.get_element(marker))
    return Pl1
for item in funcion(Pl, 3):
    print(item)
            