from Tablero import*
from random import*
from copy import*
import math
from time import*

#Aglritmo Genetico
def GA(tablero):
    time1 = time()
    #Definimos la poblacion en 500
    Npoblacion=500
    tiempo=0
    Poblacion=[]
    Apex=False
    Poblacion.append(tablero)
    ListH = []
    #Ademas de la tabla original, llenamos a la poblacion de tablas aleatorias
    for i in range(0,Npoblacion):
        Poblacion.append(Tablero(tablero.size))
    Poblacion.sort(key=lambda x: x.pares_reinas_atacadas)
    ListH.append(Poblacion[0].pares_reinas_atacadas)
    #Mientras no encuentre un indiviuo apto, o haga menos de 2500 iteraciones el bucle seguires
    while not Apex and tiempo<2500:
        #Cruza a los elementos, luego los ordena segun su valor de fitness y recorta los peores
        Poblacion=Cruzar(Poblacion,Npoblacion)
        Poblacion.sort(key=lambda x: x.pares_reinas_atacadas)
        Poblacion=Poblacion[:Npoblacion]
        ListH.append(Poblacion[0].pares_reinas_atacadas)
        
        #si el primer elemento no tiene reinas atacandose, conseguimos la solucion
        if Poblacion[0].pares_reinas_atacadas==0:
            Apex=True
        
        tiempo+=1
    time2 = time()
    return [Poblacion[0].posiciones, tiempo,Poblacion[0].pares_reinas_atacadas,time2-time1, ListH]

#Algoritmo de cruze
def Cruzar(Poblacion, npoblacion):
    n=len(Poblacion[0].posiciones)
    #La mejor mitad de la poblacion se curzara al azar entre si, en un punto al azar.
    for i in range(0,math.floor(npoblacion*50/100)):
        r=randint(0,n)
        p1=randint(0,npoblacion*50/100)
        p2=randint(0,npoblacion*50/100)
        Ntabla=Poblacion[p1].posiciones[:r]+Poblacion[p2].posiciones[r:n]

        if random()<0.5:
            Ntabla[randint(0,n-1)]=randint(0,n-1)

        Poblacion.append(Tablero(n,Ntabla))
        
    return Poblacion