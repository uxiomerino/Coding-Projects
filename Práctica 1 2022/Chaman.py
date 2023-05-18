# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:06:04 2022

@author: silvu
"""

import random as rand
from Caster import *
from Melee import *

class Chaman(Melee, Caster):
    """Establecemos la subclase Chaman"""
    def __init__(self, name, life, strength, protection, mana, shield):
        """ Establecemos as características propias da subclase Priest """
        Melee.__init__(self, name, life, strength, protection, shield)
        Caster.__init__(self, name, life, strength, protection, mana)
    
    def __str__(self):
        res = "{}".format(self.name)
        return res
    
    def defend(self):
        """Establecemos o valor da defensa do Chaman sumando a vida e o escudo"""
        defence= self.shield+self.life
        return defence
    
    def attack(self):
        """ Establecemos o valor do ataque do Chaman"""
        return self.strength
        
    def heal(self):
        """Definimos a funcion heal do Priest para curarse a cambio de mana"""
        
        # Obtemos o 50% de probabilidade de incremento do mana a través do random entre 0 e 1
        Addmana = rand.randint(0,1)
        if Addmana == 1:
            self.mana+= 2
            
        # Comprobamos o valor do mana e realizamos as operacion en consecuencia
        if self.mana > 2:
            heal = self.attack() // 3
            self.mana -= 2
        else: 
            heal = 0
            
        vida = self.life + heal
        
        self.life = vida
        
        return heal
    
    def __str__(self):
        res = "{}".format(self.name)
        return res