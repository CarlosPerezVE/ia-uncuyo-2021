from math import e
from random import*
from Tablero import*
from time import*

def SimulatedAnnealing(tablero):
    #Variebles de tiempo y contador de estados revisados
    time1 = time()
    len = tablero.size
    temp = 1
    cont = 1
    ListH = []
    ListH.append(tablero.pares_reinas_atacadas)
    while True:
        #La temepratura ba bajando con el tiempo
        T = 1/temp-0.0001
        #Cuando la temperatura llega a 0, el algoritmo termina su ejecucion y devuelve el estado actual
        if T == 0:
            time2 = time()
            return [tablero.posiciones, cont, tablero.pares_reinas_atacadas, time2-time1]

        #Se eligen un estado vecino al azar
        i = randint(0,len-1)
        j = randint(0,len-1)
        PosicionesAux = tablero.posiciones.copy()
       
        if PosicionesAux[i]     != j:
            PosicionesAux[i] = j
                    
            NuevoH = FuncionH(PosicionesAux)
            DeltaE = tablero.pares_reinas_atacadas - NuevoH
            #Si es mejor que el estado actual se cambia, si es peor se cambia con una probabilidad que disminuye con el tiempo, es 
            #decir cada vez agarra menos estados peores
            if DeltaE > 0:
                tablero.pares_reinas_atacadas = NuevoH
                tablero.posiciones = PosicionesAux.copy()
                cont = cont + 1
                ListH.append(NuevoH)
            else:
                if random() <= e**(DeltaE/T):
                    tablero.pares_reinas_atacadas = NuevoH
                    tablero.posiciones = PosicionesAux.copy()
                    cont = cont + 1
                    ListH.append(NuevoH)
                        
        temp = temp + 1

        #Si encuentra una solucion optima la envia y termina su ejecucion
        if tablero.pares_reinas_atacadas == 0:
            time2 = time()
            return [tablero.posiciones, cont, tablero.pares_reinas_atacadas, time2-time1, ListH]

