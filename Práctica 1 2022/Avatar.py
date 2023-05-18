# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:41:04 2022

@author: Uxío Merino Currás (uxio.merino@udc.es) e Iago Blanco Iglesias (iago.blancoi@udc.es)
"""


class Avatar():
    """ Establece a superclase Avatar """
    def __init__(self, name: str, life: int, strength: int, protection:int):
        """ Establece os atributos comúns a todas as subclases """
        self.name = name
        self.life = life
        self.strength = strength
        self.protection = protection
    
    def get_life(self):
        """ Devolve a vida do Avatar"""
        return ( self.life )
    
    def set_life (self, life):
        """ Modifica a vida do Avatar"""
        self.life = life
        
    def get_name(self):
        """ Devolve o nome do Avatar """
        return ( self.name )
    
    def set_name(self, name):
        """ Modifica o nome do Avatar """
        self.name = name
        
    def get_strength(self):
        """ Devolve a forza do Avatar """
        return ( self.strength )
    
    def set_strength(self, strength):
        """ Modifica a forza do Avatar """
        self.strength = strength
        
    def get_protection(self):
        """ Devolve a protección do Avatar """
        return ( self.protection)
    
    def set_protection(self, protection):
        """ Modifica a protección do Avatar """
        self.protection = protection        
    
    def attack(self):
        pass
    
    def defend(self):
        pass