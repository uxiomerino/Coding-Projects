# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:41:11 2022

@author: Uxío Merino Currás (uxio.merino@udc.es) e Iago Blanco Iglesias (iago.blancoi@udc.es)
"""
import random as rand
from Caster import *
    
class Mage(Caster):
    """ Establecemos a subclase Mage """
    
    def __innit__(self, name, life, strength, protection, mana):
        """ Establece os atributos da subclase Mage """
        super().__init__(name, life, strength, protection, mana)
        
    def __str__(self):
        res = "{}".format(self.name)
        return res
                
    def attack(self):
        """ Establecemos o valor do ataque do Mage """
        
        # Obtemos o 50% de probabilidade de incremento do mana a través do random entre 0 e 1
        Addmana = rand.randint(0,1)
        if Addmana == 1:
            self.mana = self.get_mana() + 2 
        
        # Comprobamos o valor do mana e axustamos o valor do ataque en función del
        if self.mana > 1:
            attack = self.strength 
        else:
            attack = 1
       
        # Restamos unha unidade ao valor do mana ata chegar ao valor minimo (1)
        a = self.mana - 1  
        if a < 0:
            self.mana = 1
        else : 
            self.mana = a
        
        return attack
    
    def defend(self):
        """ Devolvemos o valor da defensa """
        
        return self.protection
            
            
    