# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:33:21 2022

@author: Uxío Merino Currás (uxio.merino@udc.es) e Iago Blanco Iglesias (iago.blancoi@udc.es)
"""

# Importamos os módulos e hiperclases necesarias
import random as rand
from Melee import *

class Warrior(Melee):
    """Establecemos a subclase Warrior"""
    def __init__(self, name, life, strength, protection, shield, fury: int):
        """ Establecemos as características propias da subclase Warrior """
        super().__init__(name, life, strength, protection, shield)
        self.fury = fury
        
    def __str__(self):
        res = "{}".format(self.name)
        return res
                    
    def set_fury(self, fury):
        """ Modifica o valor do atributo fury """
        self.fury = fury
        
    def get_fury(self):
        """ Devolve o valor do atributo fury """
        return self.fury
    
    def attack(self):
        """ Función de ataque """
        f = rand.randint(0, self.fury)
        attack = f + self.strength
        
        return attack 
    
    def defend(self):
        """ Función de defensa """
        defence = self.protection + self.shield
        
        return defence
    