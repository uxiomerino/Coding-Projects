# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:38:13 2022

@author: Uxío Merino Currás (uxio.merino@udc.es) e Iago Blanco Iglesias (iago.blancoi@udc.es)
"""

from Avatar import *

class Caster(Avatar):
    """ Introduce a subclase Caster """
   
    def __init__(self, name, life, strength, protection, mana: int):
        """ Atributos específicos da subclase Caster """
        Avatar.__init__(self, name, life, strength, protection)
        self.mana = mana
    
    def set_mana(self, mana):
        """ Modifica o valor do atributo mana """
        self.mana = mana
        
    def get_mana(self):
        """ Establece o valor do atributo mana """
        return self.mana
    
        
    