import sys
import random as rand
import statistics as stats
import numpy as np

from Avatar import *
from Caster import *
from Melee import *
from Warrior import *
from Mage import *
from Chaman import *
from Priest import *

def run(path):
     with open(path) as f:
        pjs = f.readlines()
        for pj in pjs:
            parse_params(pj.split())
            
# Creamos listas para gardar os obxectos dispoñíbeis de cada categoría 
warriors = []
mages = []
priests = []
chamans = []
   
def parse_params(params):
    """ Función para crear os avatares do xogo e agregalos a listas """
    name, life, strength, protection = params[1], int(params[2]), int(params[3]), int(params[4])
    
    if params[0].lower() == "warrior":
        shield = int(params[5])
        fury = int(params[6]) 
        name = Warrior(name, life, strength, protection, shield, fury)
        warriors.append(name)
        
    elif params[0].lower() == "mage":
        mana = int(params[5])
        name = Mage(name, life, strength, protection, mana)
        mages.append(name)
        
    elif params[0].lower() == "priest":
        mana = int(params[5])
        name = Priest(name, life, strength, protection, mana)
        priests.append(name)
        
    elif params[0].lower() == "chaman":
        shield = int(params[5])
        mana = int(params[6])
        name = Chaman(name, life, strength, protection, mana, shield)
        chamans.append(name)
        
    else: 
        raise ValueError("Avatar '{}' is not valid".format(name))  

def clases_posibles(warriors, mages, priests, chamans):   
    """ Función que distingue cantas clases están dispoñibles, xa que dependen do ficheiro utilizado """
    clases = []
    if len(warriors) > 0:
        clases.append(warriors)
    if len(mages) > 0:
        clases.append(mages)
    if len(priests) > 0:
        clases.append(priests)
    if len(chamans) > 0:
        clases.append(chamans)     
        
    return clases
    
def eleccion_combatientes(warriors, mages, priest, chamans):
    """ Función para escoller aleatoriamente os combatientes """
    clases = clases_posibles(warriors, mages, priests, chamans)
         
    # Escollemos a clase de cada combatinte de maneira aleatoria
    a = rand.randint(0, len(clases)-1)
    b = rand.randint(0, len(clases)-1)
    
    clase_atacante = clases[a]
    clase_defensor = clases[b]

    # Escollemos o atacante concreto de cada clase
    at = rand.randint(0, len(clase_atacante)-1)
    de = rand.randint(0, len(clase_defensor)-1)

    atacante = clase_atacante[at]
    defensor = clase_defensor[de]

    
    # Devolvemos os datos necesarios para as seguintes funcións
    return atacante, defensor, clase_atacante, clase_defensor

def combat(warriors: list, mages: list, priests:list, chamans:list):
    """ Simula un combate """
    # Obtemos os combatientes necesarios a partir da función anterior
    args = eleccion_combatientes(warriors, mages, priests, chamans)
    
    atacante = args[0]
    defensor = args[1]
    clase_atacante = args[2]
    clase_defensor = args[3]
    
    # Se o atacante é un priest o un chaman, decidimos se loitan ou se curan
    if clase_atacante == priests or clase_atacante == chamans:
        decision = rand.randint(0, 3)
        # 25% de posibilidades de curarse
        if decision == 0:
            aumento = atacante.heal()
            dano = 0
        else:
            # Obtemos os atributos de ataque e defensa e calculamos o dano
            ataque = atacante.attack() 
            defensa = defensor.defend()
            dano = ataque - defensa
            aumento = 0
    else:
        # Obtemos os atributos de ataque e defensa e calculamos o dano
        ataque = atacante.attack()
        defensa = defensor.defend()
        dano = ataque - defensa
        aumento = 0
        
    # Calculamos a vida restante do defensor tras o combate   
    if dano > 0:
        defensor.set_life(defensor.get_life() - dano)
        vida = defensor.get_life() 
    else: 
        vida = defensor.get_life()
        dano = 0
    
     # Eliminamos ao defensor se non lle queda vida
    if vida <= 0:
        if clase_defensor == warriors:
            warriors.remove(defensor)
        elif clase_defensor == mages :
            mages.remove(defensor)
        elif clase_defensor == priests :
            priests.remove(defensor)
        else:
            chamans.remove(defensor)
          
    # Devolvemos os atributos necesarios para as seguintes funcións
    return dano, aumento, atacante, defensor, vida, clase_atacante, clase_defensor
   
def simulacion(warriors, mages, priests, chamans):
    """ Realiza simulacións de combates ata que só quede un combatinte """ 
    # Introducimos unha serie de listas e variables para poder devolver as estadísticas
    combates = 1
    danos = []
    curacions = []
    clases_gañadores = []
    dano_warriors = []
    dano_mages = []
    dano_priests = []
    dano_chamans = []
    clases = clases_posibles(warriors, mages, priests, chamans)
    
    # Bucle para executar o combate ata que só quede un avatar
    while len(warriors) + len(mages) + len(priests) + len(chamans) > 1 :
        result = combat(warriors, mages, priests, chamans) # Combate
        # Obtemos os atributos da función anterior
        dano = result[0]
        danos.append(dano)
        curacion = result[1]
        curacions.append(curacion)
        atacante = result[2]
        defensor = result[3]
        vida = result[4]
        clase_atacante = result[5]
        clase_defensor = result[6]
        
        # Calculamos o gañador 
        if vida <= 0:
            gañador = atacante
            clase_gañador = clase_atacante
        else:
            gañador = defensor
            clase_gañador = clase_defensor
            
        
             
        clases_gañadores.append(clase_gañador)
         
        # Engadimos o dano realizado á lista da súa clase    
        if clase_atacante == warriors :
            dano_warriors.append(dano)
        elif clase_atacante == mages :
            dano_mages.append(dano)
        elif clase_atacante == priests :
            dano_priests.append(dano)
        elif clase_atacante == chamans:
            dano_chamans.append(dano)
            
        combates += 1
    
    # Calculamos os valores medios dos datos a devolver
    dano_medio = stats.mean(danos)
    curacions_medias = stats.mean(curacions)
    danow_medio = stats.mean(dano_warriors)
    danom_medio = stats.mean(dano_mages)
    # So calculamos as medias destas clases se estas están dipoñibles
    if len(clases) == 3:
        danop_medio = stats.mean(dano_priests)
    elif len(clases) == 4 : 
        danop_medio = stats.mean(dano_priests)
        danoc_medio = stats.mean(dano_chamans)
    
    # O último combatiente é o campeón, e o eliminamos da lista para poder reiniciar os xogadores nas demais funcions
    for item in clases:
        if len(item) != 0:
            campeon = item[0]
            item.remove(campeon)
    # Devolvemos os atributos para as seguintes funcións tendo en conta as clases dispoñibeis
    if len(clases) == 3:
        return campeon, dano_medio, curacions_medias, clase_gañador, combates, danow_medio, danom_medio, danop_medio
    elif len(clases) == 4:
        return campeon, dano_medio, curacions_medias, clase_gañador, combates, danow_medio, danom_medio, danop_medio, danoc_medio
    else:
        return campeon, dano_medio, curacions_medias, clase_gañador, combates, danow_medio, danom_medio
    
def simulacion_20(warriors:list, mages:list, priests, chamans):
    """ Realiza a simulación de n combates """
    # Creamos unhas listas para logo poder sacar as estadísticas a partir delas
    danos_medios = []
    campeones = []
    clases_gañadores = []
    curacions_medias = []
    combates_medios = []
    victorias_clases = []
    dw_medio = []
    dm_medio = []
    dp_medio = []
    dc_medio = []
    
    for i in range(20):
        # Facemos a simulación: 
        resultado = simulacion(warriors, mages, priests, chamans)
        # Entre unha simulación e outra, restauramos os personaxes e os seus atributos iniciais
        run(sys.argv[1])
        # Obtemos os resultados da simulación
        campeon = resultado[0]
        campeones.append(campeon) 
        
        danos = resultado[1]
        danos_medios.append(danos)
       
        curacions = resultado[2]
        curacions_medias.append(curacions)
         
        clase_gañador = resultado[3]
        clases_gañadores.append(clase_gañador)
        
        combates = resultado[4]
        combates_medios.append(combates)
        
        dw = resultado[5]
        dw_medio.append(dw)
        
        dm = resultado[6]
        dm_medio.append(dm)
        # Calculamos que clases estan dispoñibeis e obtemos os resultados das que sexa pertinente
        clases = clases_posibles(warriors, mages, priests, chamans)
        if len(clases) == 3:
            dp = resultado[7]
            dp_medio.append(dp)
        elif len(clases) == 4:
            dp = resultado[7]
            dp_medio.append(dp)
            dc = resultado[8]
            dc_medio.append(dc)
       
    
    # Calculamos as medias dos datos
    media_dano = stats.mean(danos_medios)
    media_curacions = stats.mean(curacions_medias)
    medias_clases = []
    dano_medio_w = stats.mean(dw_medio)
    medias_clases.append(dano_medio_w)
    dano_medio_m = stats.mean(dm_medio)
    medias_clases.append(dano_medio_m)
    # De novo comprobamos se é necesario calcular a media de todas as clases
    if len(clases) == 3:
        dano_medio_p = stats.mean(dp_medio)
        medias_clases.append(dano_medio_p)
    elif len(clases) == 4:
        dano_medio_p = stats.mean(dp_medio)
        medias_clases.append(dano_medio_p)
        dano_medio_c = stats.mean(dc_medio)
        medias_clases.append(dano_medio_c)

    media_combates = stats.mean(combates_medios)
    for item in clases:
        n = clases_gañadores.count(item)
        victorias_clases.append(n)
    # Devolvemos as estadísticas calculadas das clases pertinentes
    print("\nESTADÍSTICAS (conxuntas das 20 simulacións):\n\nDano medio por combate: {}\nAumento de vida medio: {}".format(media_dano, media_curacions))
    if len(clases) == 2:
        print("\nVictorias de cada clase: \nWarriors = {} ({}%)\nMages = {} ({}%))".format(victorias_clases[0], victorias_clases[0]/20 * 100, victorias_clases[1], victorias_clases[1]/20 * 100))
        print("\nDano medio por clase: \nWarriors = {} \nMages = {} ".format(medias_clases[0], medias_clases[1]))
    elif len(clases) == 3:
        print("\nVictorias de cada clase: \nWarriors = {} ({}%)\nMages = {} ({}%)\nPriests = {} ({}%)".format(victorias_clases[0], victorias_clases[0]/20 * 100, victorias_clases[1], victorias_clases[1]/20 * 100,victorias_clases[2],victorias_clases[2]/20 * 100))
        print("\nDano medio por clase: \nWarriors = {} \nMages = {} \nPriests = {} ".format(medias_clases[0], medias_clases[1], medias_clases[2]))
    elif len(clases) == 4: 
        print("\nVictorias de cada clase: \nWarriors = {} ({}%)\nMages = {} ({}%)\nPriests = {} ({}%)\nChamans = {} ({}%)".format(victoriasy_clases[0], victorias_clases[0]/20 * 100, victorias_clases[1], victorias_clases[1]/20 * 100,victorias_clases[2],victorias_clases[2]/20 * 100, victorias_clases[3], victorias_clases[3]/20 * 100))
        print("\nDano medio por clase: \nWarriors = {} \nMages = {} \nPriests = {} \nChamans = {} ".format(medias_clases[0], medias_clases[1], medias_clases[2], medias_clases[3]))
    
    print("\nNúmero medio de combates que tiveron lugar: {}".format(media_combates))


def menu_inicio():
    """ Creamos un menú de inicio para que o usuario escolla que función quere executar """
    
    print("1: Combate entre dous combatientes aleatorios \n2: Combates aleatorios ata que só quede un xogador")
    print("3: Simulación de n combates para visualizar estadísticas sobre os mesmos")
    eleccion = input("Introduzca o número da opción que desexa executar: ")
    
    if eleccion == '1':
         run(sys.argv[1])
         # Executamos a función de combate 
         combate = combat(warriors, mages, priests, chamans)
    
         dano = combate[0]
         curacion = combate[1]
         atacante = combate[2]
         defensor = combate[3]
         vida = combate[4]
        
         if vida > 0:
            gañador = defensor
         else:
            gañador = atacante
            
         if curacion != 0 :
            print("\n {} decidiu aumentar a súa vida en {} unidades en lugar de atacar a {}.".format(atacante, curacion, defensor))
         else:
             print("\n{} atacou a {} e realizou un dano de {} unidades, saindo vencedor {}.".format(atacante, defensor, dano, gañador))
         seguir = input(("\n Desexa seguir probando o noso xogo? [y/n] \n"))
         
         if seguir == 'y':
            menu_inicio()
            
    elif eleccion == '2':
        run(sys.argv[1])
        sim = simulacion(warriors, mages, priests, chamans)
        
        gañador = sim[0]
        dano_medio = sim[1]
        curacions_medias = sim[2]
        combates = sim[4]
        
        print("\nO único combatiente en pe é {}.".format(gañador))
        print("\nESTADÍSTICAS: \nO dano medio realizado por combate foi {}, mentres que a media de aumento de vida por combate foi {}. Celebráronse {} combates.".format(dano_medio, curacions_medias, combates))
    
    
        seguir = input(("\n Desexa seguir probando o noso xogo? [y/n]"))
        if seguir == 'y':
            menu_inicio()
            
    elif eleccion == '3':
        run(sys.argv[1])
        simulacion_20(warriors, mages, priests, chamans)
        
        seguir = input(("\n Desexa seguir probando o noso xogo? [y/n]"))
        if seguir == 'y':
            menu_inicio()
            
    else:
         print("\n A súa elección non está entre as posibilidades. Revise o menú e volva a intentalo. ")
         menu_inicio()
        
if __name__ == "__main__":
    print("Benvido á versión de proba do noso novo videoxogo de combates! \nEstás son as opcións dispoñíbeis: ")    
    # Creamos os avatares necesarios para todo o xogo
    run(sys.argv[1])
    # Iniciamos o menú do xogo
    menu_inicio()