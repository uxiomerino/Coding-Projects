# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:20:57 2022

@author: silvu
"""

import random as rand
from Caster import *

class Priest(Caster):
    """Establecemos a subclase Priest"""
    def __init__(self, name, life, strength, protection, mana):
        """ Establecemos as características propias da subclase Priest """
        super().__init__(name, life, strength, protection, mana)
       
    def __str__(self):
        res = "{}".format(self.name)
        return res
    
    def attack(self):
        """ Función de ataque """
        
        # Obtemos o 50% de probabilidade de incremento do mana a través do random entre 0 e 1
        Addmana = rand.randint(0,1)  
        if Addmana == 1:
            self.mana+= 2 
        
        # Comprobamos o valor do mana e axustamos o valor do ataque en función del
        if self.mana > 1:
            attack = self.strength 
        else: 
            attack = 1
       
        # Restamos unha unidade ao valor do mana ata chegar ao valor minimo (1) e para que nunca sexa menor de cero
        a = self.mana - 1 
        if a < 0:
            self.mana = 1
        else : 
            self.mana = a
       
        
        return attack
    
    
        
    def defend(self):
        """Establecemos o valor da defensa do Priest"""
        return self.protection
    
    
    def heal(self):
        """Definimos a funcion heal do Priest para curarse a cambio de mana"""
        
        # Obtemos o 50% de probabilidade de incremento do mana a través do random entre 0 e 1
        Addmana = rand.randint(0,1)
        if Addmana == 1:
            self.mana+= 2
            
        # Comprobamos o valor do mana e realizamos as operacion en consecuencia
        if self.mana > 2:
            heal = self.attack() // 2
            self.mana -= 2
        else:  
            heal = 0
            
        vida = self.life + heal
        
        self.life = vida
        
        return heal
        
    def __str__(self):
        res = "{}".format(self.name)
        return res     
        
        
        
        
        
        
        
        
        
        