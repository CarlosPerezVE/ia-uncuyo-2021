from Tablero import*
from time import*
from random import*

#Variable global para guardar n de estados en la recursion
Estados = 0

#Funcion Wrapper
def QueenBT(size):

    time1 = time()
    t=Tablero(size)
    t.posiciones[0]=randint(0,size-1)
    Solucion = QueenCSP(t,1)
    time2 = time()
    Solucion.append(time2-time1)
    
    return Solucion

#Funcion Reinas con Backtraking
def QueenCSP(tablero, value):
    global Estados

    if (None not in tablero.posiciones) == True:
        return [tablero.posiciones, Estados]

    for i in range(0,len(tablero.posiciones)):
        PosAux = tablero.posiciones.copy()
        PosAux[value] = i

        if FuncionH(PosAux) == 0:
            
            TabAux = Tablero(len(tablero.posiciones))
            TabAux.posiciones = PosAux.copy()
            value = VMR(TabAux.posiciones)
            Estados = Estados + 1
            val = QueenCSP(TabAux, value)

            if val != None:
                return val