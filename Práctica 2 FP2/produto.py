# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:21:22 2022

@author: uxiom
"""

class Produto:
    """ Creamos a clase produto """
    def __init__(self, tipo):
        """ Inicializamos dita clase """
        self.tipo = tipo
        
    def get_tipo(self):
        """ Función que devolve o tipo do produto """
        return self.tipo

        