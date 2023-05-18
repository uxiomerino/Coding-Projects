# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:27:17 2022

@author: uxiom
"""

class Cliente:
    """ Creamos a clase Cliente """
    def __init__(self, repetidor, produto, idade):
        """ Inicializamos a clase Cliente """
        self.repetidor = repetidor
        self.produto = produto
        self.idade = idade
        
    def set_repetidor(self, repetidor):
        """ Establece se o cliente leva esperando un día polo seu producto """
        self.repetidor = repetidor
    
    def get_repetidor(self):
        """ Devolve 0 ou 1 dependendo de se é un cliente doutro día ou novo """
        return self.repetidor 
    
    def set_produto(self, produto):
        """ Establece o tipo de produto que o cliente quere comprar """
        self.produto = produto
    
    def get_produto(self):
        """ Devolve o valor do producto que quere comprar o cliente"""
        return self.produto
    
    def set_idade(self, idade):
        """ Establece a idade do cliente como un valor do 0 a 100"""
        self.idade = idade
    
    def get_idade(self):
        """ Devolve a idade do cliente"""
        return self.idade