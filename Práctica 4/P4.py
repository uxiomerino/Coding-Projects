# Importamos os módulos necesarios
from avl_tree import *
from array_ordered_positional_list import ArrayOrderedPositionalList as PositionalList

def mostrarCarta(Carta):
    """ Función para mostrar a AVL de maneira organizada """ 
    for item in Carta.keys(): # Recorremos as chaves da carta, é dicir, os nomes postres
        ingr = Carta[item] # Obtemos os ingredientes do postre
        pos = ingr.first() # Collemos como posición a primeira da lista de ingredientes
        print("\nPostre: {}".format(item))
        for i in range(len(Carta[item])): # Imprimimos os ingredientes de cada postre
            print("Ingrediente número {}: {} ({} unidades)".format(i+1, Carta[item].get_element(pos)[0], Carta[item].get_element(pos)[1]))
            pos = ingr.after(pos) # Retrasamos unha posición
    return Carta

def read_desserts(res, path):
    """ Abrimos o arquivo cos datos proporcionados e creamos a carta """
    Carta = AVL() # Creamos unha árbore AVL baleira coma carta
    nomes = [] # Lista baleira para a comprobación de se o postre xa existe
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split("\t")
            name, ingredient, quantity = ls[0], ls[1], int(ls[2]) # Obtemos os datos do arquivo
            if name not in nomes: # Comprobamos se o postre xa foi empezado  
                Ingredientes = PositionalList() # Creamos a lista posicional baleira cos ingredientes de cada postre (só se o postre é novo)
                nomes.append(name) # Engadímolo á lista de comprobación   
            Ingredientes.add([ingredient, quantity]) # Engadimos á lista posicional o ingrediente coa cantidade unidos nunha lista
            Carta[name] = Ingredientes # Engadimos o postre cos ingredientes ao árbore
        print("\nPostres do restaurante {}:". format(res))
        mostrarCarta(Carta) # Mostramos a carta resultante
    return Carta

def xuntar_arbores(CartaA, CartaB):
    """ Función para xuntar ambas Cartas (ambas en AVL) """
    CartaC = AVL() # Creamos unha árbore AVL baleira coma carta
    for item in CartaA.keys(): # Recorremos a carta A
        if item in CartaB.keys(): # Comprobamos que postres de A están tamén en B
            if len(CartaA[item]) > len(CartaB[item]):
                CartaC[item] = CartaB[item] # Quedámonos co postre de menor núm de ingredientes para a carta común
            else:
                CartaC[item] = CartaA[item]
    for i in CartaA.keys(): # Recorremos de novo a carta A 
       if i not in CartaB.keys():
           CartaC[i] = CartaA[item] # Engadimos á carta común os postres de A que non estén en B
    for j in CartaB.keys(): # Recorremos a carta B
        if j not in CartaA.keys(): # Comprobamos que o postre non esté en A
            CartaC[j] = CartaB[item] # Engadimos o postre á carta común
    print("\n\nCarta da mezcla dos restaurantes A e B: ")
    mostrarCarta(CartaC) # Mostramos a carta común
    return CartaC

def carta_min(CartaA, CartaB):
    """ Función para obter os postres comúns de ambas Cartas """
    CartaMin = AVL() # Creamos unha árbore baleira para almacenar a carta mínima
    for item in CartaA.keys(): # Recorremos a carta A 
        if item in CartaB.keys(): # Comprobamos que o postre está na carta B
            if len(CartaA[item]) > len(CartaB[item]):
                CartaMin[item] = CartaB[item] # Quedámonos co postre de menor núm de ingredientes para a carta común
            else:
                CartaMin[item] = CartaA[item]
    print("\n\nCarta mínima da mezcla dos restaurantes A e B: ")
    mostrarCarta(CartaMin)
    return CartaMin

if __name__ == "__main__":
    # Comprobamos que versión da carta A quere o usuario fusionar
    carta = int(input("Introduzca a versión da Carta do restaurante A que quere fusionar (1 ou 2): "))
    if carta == 1:
        ruta = "recetarioA.txt"
    elif carta == 2:
        ruta = "recetarioA2.txt"
    else: 
        print("A opción introducida non está entre as opcións.")
    CartaA = read_desserts(res = 'A', path = ruta)
    print("\n-------------------------\n-------------------------")
    CartaB = read_desserts(res = 'B', path = "recetarioB.txt")
    print("\n-------------------------\n-------------------------")
    CartaC = xuntar_arbores(CartaA, CartaB)
    print("\n-------------------------\n-------------------------")
    CartaMin = carta_min(CartaA, CartaB)
    