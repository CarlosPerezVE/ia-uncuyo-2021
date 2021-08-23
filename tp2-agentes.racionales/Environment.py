from random import *
import numpy

class Environment:

    def __init__(self,sizeX,sizeY,dirt_rate):
        self.sizeX= sizeX
        self.sizeY= sizeY
        self.posX= randint(0,sizeX-1)
        self.posY= randint(0,sizeY-1)
        self.performance=0
        self.grilla=numpy.zeros((sizeX,sizeY))
        self.contdirt=0 #contador de tierra auxiliar

        #Rellena aleatoriamente la grilla hasta que haya el numero de casillas necesarias
        while self.contdirt<round(sizeY*sizeX*dirt_rate):
            x=randint(0,sizeX-1)
            y=randint(0,sizeY-1)
            if self.grilla[x][y]==0:
                self.grilla[x][y]=1
                self.contdirt=self.contdirt+1

    #Chequea si una accion es valida
    def accept_action(self,action):
        if action == 'clean' and self.grilla[self.posX][self.posY]==1:
            return True
        elif action == 'up' and self.posX>0:
            return True
        elif action == 'down' and self.posX<self.sizeX-1:
            return True
        elif action == 'left' and self.posY>0:
            return True
        elif action =='right'and self.posY<self.sizeY-1:
            return True
        elif action == 'idle':
            return True
        else:
            return False

    def is_dirty(self):
        if self.contdirt!=0:
            return True

    def get_performance(self):
        return self.performance


  