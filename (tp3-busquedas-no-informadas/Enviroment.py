from random import *
import numpy

class Enviroment:

    def __init__(self):
        self.agentPos= [randint(0,99),randint(0,99)]
        self.objetivo= [randint(0,99),randint(0,99)]
        self.grilla=numpy.full((100,100),'C')  #Crea una grilla llena de casillas 'C' de 100x100
        for i in range(0,100):
            for j in range(0,100):
                if random() <= 0.2:
                    if (i != self.agentPos[0] and j!= self.agentPos[1]) and (i != self.objetivo[0] and j != self.objetivo[1]):
                        self.grilla[i][j]='O' #Añade aleatoriamente obstaculos a la grilla


    #Chequea si una accion de movimiento es valida
    def accept_action(self,X,Y,action):
        if action == "up":
            if X > 0 and self.grilla[X-1][Y] == 'C':
                return True
            else:
                return False
        elif action == "down":
            if X < 99 and self.grilla[X+1][Y] == 'C':
                return True
            else:
                return False
        elif action == "right":
            if Y < 99 and self.grilla[X][Y+1] == 'C':
                return True
            else:
                return False
        elif action == "left":
            if Y > 0 and self.grilla[X][Y-1] == 'C':
                return True
            else:
                return False


  