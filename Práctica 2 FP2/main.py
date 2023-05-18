# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:00:24 2022

@author: uxiom
"""

from array_queue import *
from cliente import Cliente
import random as rand
import statistics as stats

def valores_dados():
    """ Devolve os valores dados para o desenvolvemento secuencial """
    # Datos proporcionados polo PDF
    days = 90
    cantidadeA = 100
    cantidadeB = 200
    cantidadeC = 400
    clients = 700
    # Creamos as colas dos produtos
    ProdutoA = ArrayQueue()
    ProdutoB = ArrayQueue()
    ProdutoC = ArrayQueue()
    # Creamos a cola de clientes
    Clientes = ArrayQueue()
    # Xuntamos os datos nunha lista de listas
    produtos = [['A', cantidadeA, ProdutoA], ['B', cantidadeB, ProdutoB], ['C', cantidadeC, ProdutoC]]
    clientes = [clients, Clientes]
    return days, produtos, clientes
def valores_teclado():
    """ Función para introducir un maior número de produtos """
    # Pedimos os datos por teclado ao usuario
    d = int(input("Introduzca o número de días da simulación: "))
    c = int(input("Introduzca o número de clientes diario: "))
    n_productos = int(input("Introduzca o número de productos que haberá dispoñíbeis (máx 6): "))
    # Comprobamos que o número de produtos é correcto
    assert n_productos <= 6, 'Só se poden introducir ata 6 produtos'
    # Posíbeis nomes dos produtos
    nomes_prod = ['A', 'B', 'C', 'D', 'E', 'F']
    # Creamos a lista vacía para devolver os datos
    datos = []
    # Creamos a cola de Clientes e o xuntamos nunha lista co nº de clientes introcucido por teclado
    Clientes = ArrayQueue()
    clientes = [c, Clientes]
    # Creamos as colas dos produtos e xuntamolas nunha lista xunto co nome do produto e a súa cantidade inicial
    for item in range(0, n_productos):
        prod = nomes_prod[item]
        col = ArrayQueue()
        c = int(input("Introduzca a cantidade dispoñíbel diariamente do produto {}: ".format(prod)))
        datos.append([prod, c, col])
    return d, datos, clientes

def bucle(datos, Edad = False):
    """ Realiza o bucle da simulación diaria """
    # Sacamos os datos a partir dos argumentos
    days = datos[0]
    produtos = datos[1]
    clientes = datos[2][0]
    Clientes = datos[2][1]    
    # Creamos unha nova cola para engadir aos clientes que non obtiveron o seu producto
    Repetidores = ArrayQueue()
    # Bucle diario
    for i in range(0, days):
        # Comprobamos se hai repetidores do día anterior e os engadimos en primeiro lugar á cola
        if len(Repetidores) != 0:
            for i in range(len(Repetidores)):
                c = Repetidores.first()
                Clientes.enqueue(c)
                Repetidores.dequeue()
        # Chegan os productos, creamos os obxectos da clase Produtos e engadimolos ás colas
        for item in produtos:
            for x in range(item[1]):
                item[2].enqueue(1)
        # Comprobamos se está activa a opcións especial da preferencia de idade (non existe preferencia sobre os repetidores, pero si sobre o público novo)
        if Edad == True:
            C = []
            for j in range(clientes):
                # Definimos a idade dos clientes
                idade= rand.randint(10, 100)
                client = Cliente(0, 0, idade)
                C.append(client)
            for client in C:
                # Comprobamos a idade de todos os clientes
                idade=client.get_idade()
                if idade >= 65: # Fixamos o inicio da idade de preferencia en 65
                    # Engadimos primeiro á cola os clientes que teñan 65 ou máis anos
                    Clientes.enqueue(client)
                    C.remove(client)
            # Engadimos os clientes restantes á cola
            for client in C:
                Clientes.enqueue(client)
        # Se dita opción non está activa, engadimos os clientes con normalidade
        else:
            # Chegan os clientes novos, creamos os obxectos da clase Cliente e os engadimos á cola
            for j in range(clientes):
                client = Cliente(0, 0, 0) #Ao crear os obxectos da clase Cliente, iniciamos todos os seus atributos en 0
                Clientes.enqueue(client)
        # Por orde, van facendo a súa elección de produtos
        for c in range(len(Clientes)): 
            cliente = Clientes.first()
            # Comprobamos se é repetidor, para obter o produto gardado coa clase ou asignarlle un novo
            if cliente.get_repetidor() == 1:
                produto_cliente = cliente.get_produto()
            else:
                produto_cliente = produtos[rand.randint(0, len(produtos)-1)][0]
                cliente.set_produto(produto_cliente)
            # Comprobamos o tipo de produto que é e a dispoñibilidade do mesmo
            for item in produtos:
                if produto_cliente == item[0]:
                    if len(item[2]) > 0:
                        item[2].dequeue()
                        Clientes.dequeue()
                    elif len(item[2]) == 0:
                        Clientes.dequeue()
                        cliente.set_repetidor(1)
                        Repetidores.enqueue(cliente)
        # Estadísticas
        clientes_incompletos = int(len(Repetidores))
        clientes_completados = int(days * clientes - clientes_incompletos)
        colas = []
        vendas = []
        for item in produtos:
            cola = item[2]
            colas.append(cola)
            v = (item[1] * days - len(cola)) / days
            vendas.append(v)
    return  vendas, colas, clientes_completados, clientes_incompletos
 
def opcion1(Optativa):
    """ Función con todo o necesario para mostrar as estadísticas cando os datos son os do PDF """
    # Creamos unha serie de listas que van axudar coas estadísticas
    vendasA = []
    vendasB = []
    vendasC = []
    clientes_comp = []
    clientes_incomp = []
    # Bucle para realizar 20 iteracións da simulación
    for i in range(0, 20):
        # Chamamos á función que proporciona os datos proporcionados no PDF
        datos = valores_dados()
        # Executamos a función do bucle diario
        resultado = bucle(datos, Optativa)
        # Engadimos os datos ás listas de estadísticas
        vendasA.append(resultado[0][0])
        vendasB.append(resultado[0][1])
        vendasC.append(resultado[0][2])
        clientes_comp.append(resultado[2])
        clientes_incomp.append(resultado[3])
    vendas = [vendasA, vendasB, vendasC]
    # Facemos o print das estadísticas
    for item in range(len(datos[1])): 
        print("\nProducíronse unhas ventas medias diarias do produto {} de {} unidades, cunha desviación típica de {}.". format(datos[1][item][0], stats.mean(vendas[item]), stats.pstdev(vendas[item])))
    print("O número de clientes que completaron o seu pedido (de media por cada iteración da simulación) foi de {}, cunha desviación típica de {}, mentras que os que quedaron desabastecidos foron, tamén de media por iteración da simulación, {}, con desviación típica {}.". format(stats.mean(clientes_comp), stats.pstdev(clientes_comp), stats.mean(clientes_incomp), stats.pstdev(clientes_incomp)))

def opcion2(Optativa):
    """ Función con todo o necesario para mostrar as estadísticas cando os datos son introducidos por teclado """
    # Obtemos os datos a través da función correspondente
    datos = valores_teclado()
    # Creamos listas e un diccionario para proporcionar estadísticas
    vendas = {}
    clientes_comp = []
    clientes_incomp = []
    # Enchemos o diccionario co nome do produto como chave e listas vacías nos valores 
    for item in datos[1]:
        vendas[item[0]] = []
    # Realizamos o bucle para as 20 iteracións da simulación
    for i in range(0, 20):
        # Renovamos as colas dos produtos tras cada iteración, para que empecen baleiras
        for item in datos[1]:
            col = ArrayQueue()
            item[2]= col
        # Chamamos á función principal de simulación
        resultado = bucle(datos, Optativa)
        # Obtemos os datos relevantes
        clientes_comp.append(resultado[2])
        clientes_incomp.append(resultado[3])
        for x in range(len(vendas)):
            lista = vendas[datos[1][x][0]]
            lista.append(resultado[0][x])
            vendas[datos[1][x][0]] = lista
    # Imprimimos por pantalla as estadísticas
    for item in vendas.keys(): 
        print("Producíronse unhas ventas medias diarias do produto {} de {} unidades, cunha desviación típica de {}.". format(item, stats.mean(vendas[item]), stats.pstdev(vendas[item])))
    print("\n\nO número de clientes que completaron o seu pedido (de media por cada iteración da simulación) foi de {}, cunha desviación típica de {}, mentras que os que quedaron desabastecidos foron, tamén de media por cada iteración da simulación, {}, con desviación típica {}.". format(stats.mean(clientes_comp), stats.pstdev(clientes_comp), stats.mean(clientes_incomp), stats.pstdev(clientes_incomp)))


def menu():
    """ Menú principal para poder executar as distintas versións do programa """
    
    print("Escolla o tipo de simulación que desexa probar: ")
    print("1: 20 simulacións cos datos proporcionados polo PDF \n2: 20 simulacións con datos a introducir por teclado")
    print("3: Simulacións introducindo novas características dos clientes")
    opcion = input("\nIntroduzca a opción que desexa realizar: ")
    # Chamamos ás funcións necesarias para cada opción do menú
    if opcion == '1':
        opcion1(False)
    elif opcion == '2':
        opcion2(False)
    elif opcion == '3':
        op = input("Desexa facer a simulación cos valores dados polo PDF (1) ou introducilos por teclado (2)?: ")
        if op == '1':
            opcion1(True)
        elif op == '2':
            opcion2(True)
    else:
        "\nA túa opción non está entre as posibilidades ofrecidas, volve a intentalo. \n"
        menu()
if __name__ == "__main__" :
    menu()