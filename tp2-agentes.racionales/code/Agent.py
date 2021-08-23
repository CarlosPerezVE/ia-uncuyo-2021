from random import *

class Agent:
    def __init__(self,env):
        self.env=env
        self.energy=1000

    def up(self):
        if self.env.accept_action('up'):
            self.env.posX=self.env.posX-1
            self.energy-=1

    def down(self):
        if self.env.accept_action('down'):
            self.env.posX=self.env.posX+1
            self.energy-=1

    def left(self):
        if self.env.accept_action('left'):
            self.env.posY=self.env.posY-1
            self.energy-=1

    def right(self):
        if self.env.accept_action('right'):
            self.env.posY=self.env.posY+1
            self.energy-=1

    def idle(self):
        if self.env.accept_action('idle'):
            self.energy-=1

    def suck(self):
        if self.env.accept_action('clean') and self.perspective():
            self.env.grilla[self.env.posX][self.env.posY]=0
            self.energy-=1
            self.env.contdirt-=1
            self.env.performance=self.env.performance+1
        else:
            self.energy-=1
    
    def perspective(self):
        if self.env.grilla[self.env.posX][self.env.posY]==1:
            return True

    #El agente va hacia el principio de la grilla y la recorre de izquierda a derecha, baja, y luego de izquierda a derecha
    #y asi sucesivamente
    def think(self):
        #Lleva al agente al principio
        while self.env.posY>0:
            self.left()
        while self.env.posX>0:
            self.up()
        self.suck()
        switch=0
        i=0
        j=0
        #Recorre la grilla, limpiando cuando sea necesario
        while i <self.env.sizeX and self.energy>3:
            while j <self.env.sizeY and self.energy>3:
                if switch%2==0:
                    self.right()
                    if self.perspective():
                        self.suck()
                    j+=1
                else:
                    self.left()
                    if self.perspective():
                        self.suck()
                    j+=1
            j=0
            if(self.energy>=2):
                self.down()
                if self.perspective():
                    self.suck()
                switch+=1
                i+=1

    #Funcion random
    def random(self):
        while self.energy>0:
            accion=randint(0,5)
            if accion==0:
                self.up()
            elif accion==1:
                self.right()
            elif accion==2:
                self.left()
            elif accion==3:
                self.down()
            elif accion==4:
                self.idle()
            elif accion==5:
                self.suck()
