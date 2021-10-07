from random import*
from typing import Type

#Clase tablero usando 1 sola lista
class Tablero:
    def __init__(self, size):
        self.posiciones = [None]*size
        self.pares_reinas_atacadas = 0

def FuncionH(posiciones):
    cont=0
    for i in range(len(posiciones)):
        for j in range(i,len(posiciones)):
            if posiciones[i] != None and posiciones[j] != None and type(posiciones[i]) == int and type(posiciones[j]) == int:
                if i != j:
                    if posiciones[i] == posiciones[j]:
                        cont+=1
                    elif abs(i-j) == abs(posiciones[i]-posiciones[j]):
                        cont+=1 
    return cont

#Funcion para saber el MVR
def VMR(posiciones):
    nextQueen=0
    minQueen = len(posiciones)*len(posiciones)
    for i in range (len(posiciones)):
        TableroAux = posiciones.copy()
        if TableroAux[i] == None:
            cont = 0
            for j in range(len(posiciones)):
                TableroAux[i] = j
                if FuncionH(TableroAux) == 0:
                    cont+=1
            if cont < minQueen:
                nextQueen = i
                minQueen = cont
    return nextQueen

#Encadenamiento hacia adelante

#Clase tablero usando lista de listas
class TableroFC():
    def __init__(self, size):
        self.posiciones = []
        ListaAux = []
        for i in range(size):
            ListaAux.append(i)
        for i in range(size):
            self.posiciones.append(ListaAux.copy())
        self.pares_reinas_atacadas = 0

def VMRFC(posiciones):
    lon = len(posiciones)
    nextQueen = -1
    minQueen = 999999
    for i in range(lon):
        if type(posiciones[i]) != int:
            if len(posiciones[i])<minQueen:
                minQueen = len(posiciones[i])
                nextQueen = i
    return nextQueen
