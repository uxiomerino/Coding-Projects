# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:18:00 2022

@author: Uxío Merino Currás (uxio.merino@udc.es) e Iago Blanco Iglesias (iago.blancoi@udc.es)
"""
from Avatar import *

class Melee(Avatar):
    """Establece a subclase Melee"""
    def __init__(self, name, life, strength, protection, shield: int):
        Avatar.__init__(self, name, life, strength, protection)
        self.shield = shield
    
    
    def set_shield(self, shield):
        """ Modifica o valor do atributo shield """
        self.shield = shield
        
    def get_shield(self):
        """ Devolve o valor do atributo shield """
        return self.shield
    