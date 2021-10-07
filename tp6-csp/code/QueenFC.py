from typing import Collection
from Tablero import*
from time import*
from random import*

Estados = 0

def QueenFC(size):

    time1 = time()
    tablero = TableroFC(size)
    Solucion = FC(tablero,0)
    time2 = time()
    Solucion.append(time2-time1)
    
    return Solucion


def FC(tablero, value):
    global Estados
    lon = len(tablero.posiciones)
    check = True
    for i in range(0,lon):
        if type(tablero.posiciones[i]) != int:
            check = False
    if check == True:
        return [tablero.posiciones, Estados]

    for i in range(0,len(tablero.posiciones[value])):
        PosAux = CopiarLista(tablero.posiciones)
        PosAux[value] = PosAux[value][i]
            
        TabAux = TableroFC(lon)
        TabAux.posiciones = CopiarLista(PosAux)
        ActDominio(TabAux.posiciones,value)
        value = VMRFC(TabAux.posiciones)
        
        Estados = Estados + 1
        val = FC(TabAux, value)
        if val != None:
            return val


#Saca del dominio las variables eliminadar por los arcos hacia adelante
def ActDominio(Posiciones, Columna):
    for i in range(0,len(Posiciones)):
        if i != Columna and type(Posiciones[i]) != int:
            ValEliminar = []
            for j in range(0,len(Posiciones[i])):
                    if Posiciones[Columna] == Posiciones[i][j]:
                        ValEliminar.append(Posiciones[i][j])
                    elif abs(Columna - i) == abs(Posiciones[i][j]-Posiciones[Columna]):
                        ValEliminar.append(Posiciones[i][j]) 
            for j in range(0,len(ValEliminar)):
                Posiciones[i].remove(ValEliminar[j])

def CopiarLista(Posiciones):
    lista = []
    for i in range(len(Posiciones)):
        if type(Posiciones[i]) == int:
            lista.append(Posiciones[i])
        else:
            lista.append(Posiciones[i].copy())
    return lista