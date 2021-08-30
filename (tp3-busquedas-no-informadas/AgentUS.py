import heapq 

class AgentUS:
    def __init__(self, Enviroment):
        self.env = Enviroment
        self.pos = Enviroment.agentPos
        self.obj = Enviroment.objetivo
        self.casillasFronteras = []
        heapq.heapify(self.casillasFronteras) #El US esta implementado con una cola con prioridad, heapq en python
        heapq.heappush(self.casillasFronteras,(0,self.pos))#La cola tiene una tupla que contienen la prioridad, y la posicion 
        self.env.grilla[self.pos[0],self.pos[1]]='F'

    def think(self):
        #Imprime el mapa
        print("Mapa de casillas y obstaculos: ")
        for i in range(0,99):
            for j in range(0,99):
                print(self.env.grilla[i][j],end=" ")
            print(" ")
        print(" ")
        Secuencia = Usearch(self,0)
        print("Leyenda: ")
        print("O = Obstaculo")
        print("C = Casilla")

        print(" ")
        print("Posicion inical del Agente: ", self.pos)
        print("Posicion del Objetivo: ", self.obj)
        print(" ")
        if Secuencia != None:
            print("Recorrido del agente: ")
            print(Secuencia)
        else: 
            print("No hay camino valido hacia el objetivo")

def is_next(Est1, Est2):
    Resta = [Est1[0]-Est2[0],Est1[1]-Est2[1]]
    if Resta == [0,1] or Resta == [0,-1] or Resta == [1,0] or Resta == [-1,0]:
        return True
#Algoritmo de busqueda uniforme aplicado a la grilla
def Usearch(self,cont):

        while len(self.casillasFronteras) > 0:
            Estado = heapq.heappop(self.casillasFronteras)[1]
            self.env.grilla[Estado[0]][Estado[1]] = "E"

            if Estado == self.obj:
                Lista = []
                Lista.append(Estado)
                return Lista
            else:
                #Chequea que los movimientos sean validos, en caso de serlos lo ingresa en la cola con prioridad    
                if self.env.accept_action(Estado[0],Estado[1],'up'):
                    self.env.grilla[Estado[0]-1][Estado[1]] = "F"
                    heapq.heappush(self.casillasFronteras,(cont+1,[Estado[0]-1,Estado[1]]))

                if self.env.accept_action(Estado[0],Estado[1],'down'):
                    self.env.grilla[Estado[0]+1][Estado[1]] = "F"
                    heapq.heappush(self.casillasFronteras,(cont+1,[Estado[0]+1,Estado[1]]))

                if self.env.accept_action(Estado[0],Estado[1],'right'):
                    self.env.grilla[Estado[0]][Estado[1]+1] = "F"
                    heapq.heappush(self.casillasFronteras,(cont+1,[Estado[0],Estado[1]+1]))

                if self.env.accept_action(Estado[0],Estado[1],'left'):
                    self.env.grilla[Estado[0]][Estado[1]-1] = "F"
                    heapq.heappush(self.casillasFronteras,(cont+1,[Estado[0],Estado[1]-1]))

                Lista = Usearch(self,cont+1)
                if Lista != None:
                    if is_next(Lista[0],Estado) == True:
                        Lista.insert(0,Estado)
                    return Lista

        return None