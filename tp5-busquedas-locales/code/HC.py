from Tablero import*
from time import*

def HillClimbing(tablero):
    #Definimos una variable que guarda el mejor estado
    ListH = []
    MEstado = tablero.posiciones.copy()
    Mh = FuncionH(tablero.posiciones)
    time1 = time()
    ListH.append(Mh)
    #Numero maximo de temperatura
    temp=1000
    for cont in range(temp):
        for i in range(len(tablero.posiciones)):
            #Creamer unas copia del tablero para modificar
            PosicionesAux = tablero.posiciones.copy()
            ValAux = PosicionesAux[i]
            #Recorremos el tablero y vamos intercambiando reinas, de encontrar un tablero con mejor estado, lo asigmanos como mejor H
            for j in range(len(tablero.posiciones)):
                if ValAux != j:
                    PosicionesAux[i] = j
                    NuevoH = FuncionH(PosicionesAux)
                    if NuevoH < Mh:
                        Mh = NuevoH
                        MEstado = PosicionesAux.copy()

        tablero.posiciones = MEstado
        tablero.pares_reinas_atacadas = Mh
        ListH.append(Mh)
        #Si encuentra una solucion valida, se acaba la funcion
        if tablero.pares_reinas_atacadas == 0:
            time2 = time()
            return [MEstado, cont+1 , Mh,time2-time1, ListH]
    time2 = time()
    return [MEstado, cont+1 , Mh,time2-time1, ListH] 

