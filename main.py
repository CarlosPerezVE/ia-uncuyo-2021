from typing import Counter
from HC import*
from SA import*
from Tablero import*
from GA import*
import statistics
import collections

t=0
ListaHC4=[]
ListaHC8=[]
ListaHC10=[]

ListaSA4=[]
ListaSA8=[]
ListaSA10=[]

ListaGA4=[]
ListaGA8=[]
ListaGA10=[]

for i in range(0,30):

    T4=Tablero(4)
    T4SA=Tablero(4,T4.posiciones)
    T4GA=Tablero(4,T4.posiciones)

    T8=Tablero(8)
    T8SA=Tablero(8,T8.posiciones)
    T8GA=Tablero(8,T8.posiciones)

    T10=Tablero(10)
    T10SA=Tablero(10,T10.posiciones)
    T10GA=Tablero(10,T10.posiciones)

    ListaHC4.append(HillClimbing(T4))
    ListaHC8.append(HillClimbing(T8))
    ListaHC10.append(HillClimbing(T10))

    ListaSA4.append(SimulatedAnnealing(T4SA))
    ListaSA8.append(SimulatedAnnealing(T8SA))
    ListaSA10.append(SimulatedAnnealing(T10SA))

    ListaGA4.append(GA(T4GA))
    ListaGA8.append(GA(T8GA))
    ListaGA10.append(GA(T10GA))
    

print("Hill Climbing 4x4:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaHC4[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaHC4])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaHC4])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaHC4])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaHC4])))

print("============================")

print("Hill Climbing 8x8:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaHC8[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaHC8])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaHC8])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaHC8])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaHC8])))

print("============================")

print("Hill Climbing 10x10:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaHC10[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaHC10])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaHC10])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaHC10])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaHC10])))

print("============================")

print("Simulated Annealing 4x4:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaSA4[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaSA4])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaSA4])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaSA4])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaSA4])))

print("============================")

print("Simulated Annealing 8x8:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaSA8[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaSA8])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaSA8])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaSA8])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaSA8])))

print("============================")

print("Simulated Annealing 10x10:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaSA10[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaSA10])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaSA10])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaSA10])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaSA10])))

print("============================")

print("Algoritmo Genetico 4x4:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaGA4[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaGA4])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaGA4])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaGA4])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaGA4])))
 
print("============================")

print("Algoritmo Genetico 8x8:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaGA8[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaGA8])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaGA8])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaGA8])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaGA8]))) 


print("============================")

print("Algoritmo Genetico 10x10:")
print("Porcentaje de exito:")
aux=0
for i in range(0,30):
    if ListaGA10[i][2]==0:
        aux+=1
print(str(aux*100/30)+"%")

print("Tiempo de ejecucion:")
print("Media: " + str(statistics.mean([x[3] for x in ListaGA10])))
print("Desviacion Estandar: " + str(statistics.stdev([x[3] for x in ListaGA10])))

print("Cantidad de estados:")
print("Media: " + str(statistics.mean([x[1] for x in ListaGA10])))
print("Desviacion Estandar: " + str(statistics.stdev([x[1] for x in ListaGA10]))) 
 



