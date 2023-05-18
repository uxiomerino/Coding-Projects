from array_ordered_positional_list import ArrayOrderedPositionalList as PositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList as PositionalList

def read_pantry(path="data/despensa.txt"):
    """ Abrimos o arquivo cos datos da despensa e creamos a despensa virtual cunha lista posicional """
    Despensa = PositionalList() # Creamos a lista posicional
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split("\t")
            name, quantity = ls[0], int(ls[1]) # Obtemosos os datos do arquivo
            Despensa.add([name, quantity]) # Engadímolos á lista posicional nunha lista con ambos atributos
            print("O produto {} foi engadido á despensa con {} unidades.".format(name, quantity))
    return Despensa

def read_desserts(path="data/recetario.txt"):
    """ Abrimos o arquivo cos datos do recetario e creamos a carta """
    Carta = {} # A carta vai ser un diccionario
    nomes = [] # Lista baleira para poder saber se estamos creando un postre novo ou engadindo ingredentes a un xa existente
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split("\t")
            name, ingredient, quantity = ls[0], ls[1], int(ls[2]) # Obtemos os datos do arquivo
            if name not in nomes: # Comprobamos se o postre xa existe
                Ingredientes = PositionalList() # Creamos a lista posicional baleira cos ingredientes de cada postre (só se o postre é novo)
                nomes.append(name) # Engadímolo á lista de comprobación
                
            Ingredientes.add([ingredient, quantity]) # Engadimos á lista posicional o ingrediente coa cantidade unidos nunha lista
            Carta[name] = Ingredientes # Utilizamos o nome do postre como chave do diccionario e a lista posicional de ingredientes como valor
        
        for item in Carta.keys():
            ingr = Carta[item]
            pos = ingr.first()
            print("\nPostre: {}".format(item))
            for i in range(len(Carta[item])):
                print("Ingrediente número {}: {} ({} unidades)".format(i+1, Carta[item].get_element(pos)[0], Carta[item].get_element(pos)[1]))
                pos = ingr.after(pos)
    return Carta

def read_pedidos(path="data/pedidos.txt"):
    """ Abrimos o arquivo cos pedidos e atendemos as comandas """
    Pedidos = PositionalList() # Creamos unha lista posicional para os pedidos
    print("")
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split("\t")
            mesa, comanda = ls[0], ls[1] # Obtemos os datos do arquivo de pedidos
            if comanda not in Carta.keys(): # Se o pedido non está na carta rexeitamolo
                print("\nPedido da mesa {} rexeitado: postre {} fora de carta".format(mesa, comanda))
            else:
                print("\nPedido recibido: {} para a mesa {}".format(comanda, mesa))
                Pedidos.add([mesa, comanda]) # Engadimos os datos do pedido á lista posicional nunha lista
                ingr = Carta[comanda] # Obtemos os ingrediente da carta de comandas
                falta = [] # Lista de produtos q fatan
                usados = [] # Lista de produtos usados
                for item in ingr:
                    for i in Despensa:
                        if item[0] == i[0]: # Contrastamos os ingredientes do postre coa despensa
                            if item[1] > i[1]: #Se a cantidade necesaria no postre é maior á dispoñíbel, engadimos o ingrediente á lista dos que faltan
                                falta.append([[item[0], i[1]], item[1]]) # Engadimos unha lista, cuxo primeiro valor é unha lista co nome do postre e o valor inicial para poder buscalo logo
                            else: # En caso contrario, engadimos o ingrediente á lista de usados
                                usados.append([[item[0], i[1]], item[1]])
                        
                if len(falta) > 0: # O pedido non se chegou a elaborar
                    print("Pedido rexeitado. Faltan: ")
                    for item in falta: # Obtemos o nome e as cantidades q faltan dos produtos
                        cantidade_anterior = Despensa.get_element(Despensa.search_element(item[0]))[1]
                        cantidade_actualizada = abs(cantidade_anterior - item[1])
                        print("{} en {} unidades".format(item[0][0], cantidade_actualizada))
                    Carta.pop(comanda) # Eliminamos o postre da carta
                    print("Postre eliminado.")
                else: # O pedido si se elabora
                    print("Pedido aceptado.")
                    for item in usados: # Obtemos as cantidades restantes dos produtos para actuaizar a despensa
                        cantidade_anterior = Despensa.get_element(Despensa.search_element(item[0]))[1]
                        cantidade_actualizada = cantidade_anterior - item[1]
                        if cantidade_actualizada == 0: # Se a cantidade é 0 eliminamos da carta todos os postres que conteñan ese produto
                            Despensa.delete(Despensa.search_element(item[0]))
                            print("Produto {} esgotado tras esta elaboración.".format(item[0][0]))
                            eliminar = []
                            for x in Carta.keys():
                                for y in Carta[x]:    
                                    if item[0][0] == y[0]:
                                        eliminar.append(x)
                            for i in eliminar:
                                Carta.pop(i)
                                print("Produto {} eliminado da carta: non hai ingredientes suficientes".format(i))
                        else:
                             Despensa.replace(Despensa.search_element(item[0]), [item[0][0], cantidade_actualizada])
            
    return Pedidos
    
def visualizar_carta(Carta:dict):
    """ Función para visualizar os produto dispoñibles na carta cos seus ingredientes """
    for item in Carta.keys():
        print("\nOs postres dispoñibles son: {}".format(item))
        print("Leva os seguintes ingredientes: ")
        for i in Carta[item]:
            print("{} en {} unidades". format(i[0], i[1]))


if __name__ == "__main__":

    Despensa = read_pantry()
    Carta = read_desserts() 
    Pedidos = read_pedidos()
    visualizar_carta(Carta)