from random import*

class Tablero:
    #tablero
    def __init__(self, size,posiciones=[]):
        self.size=size
        self.posiciones = [None]*size
        PosicionInicial(self.posiciones)
        self.pares_reinas_atacadas = FuncionH(self.posiciones)            


def PosicionInicial(Posiciones):
    for i in range(len(Posiciones)):
        Posiciones[i] = randint(0,len(Posiciones)-1)

    #Funcion que calcula el numero de pares de reinas atacandose
def FuncionH(Posiciones):
    cont = 0
    for i in range(len(Posiciones)):
        for j in range(i,len(Posiciones)):
            if i != j:
                if Posiciones[i] == Posiciones[j]:
                    cont = cont + 1
                elif abs(i-j) == abs(Posiciones[i]-Posiciones[j]):
                    cont = cont + 1 
        
    return cont

