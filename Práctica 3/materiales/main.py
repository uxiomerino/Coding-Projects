def read_pantry(path="data/despensa.txt"):

    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split("\t")
            ingredient, quantity = ls[0], int(ls[1])
            print ("TODO: añadir a la despensa ingrediente \"{}\" ({} unidades)".format(ingredient, quantity))

def read_desserts(path="data/recetario.txt"):

    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split("\t")
            name, ingredient, quantity = ls[0], ls[1], int(ls[2])
            print ("TODO: añadir ingrediente \"{}\" ({} unidades) al postre \"{}\""
            .format(ingredient, quantity,name))

def read_pedidos(path="data/pedidos.txt"):
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split("\t")
            mesa, comanda = ls[0], ls[1]
            print ("TODO: Nuevo pedido: {} - mesa {}".format(comanda, mesa))

if __name__ == "__main__":

    read_pantry()
    read_desserts() 
    read_pedidos()