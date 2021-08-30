import queue

class AgentBFS:
    def __init__(self, Enviroment):
        self.env = Enviroment
        self.pos = Enviroment.agentPos #posicion del agente
        self.obj = Enviroment.objetivo #posicion del objetivo
        self.casillasFronteras = queue.Queue() #Cola fifo
        self.casillasFronteras.put(self.pos)
        self.env.grilla[self.pos[0],self.pos[1]]='F'

    def think(self):
        #Imprime el mapa
        print("Mapa de casillas y obstaculos: ")
        for i in range(0,99):
            for j in range(0,99):
                print(self.env.grilla[i][j],end=" ")
            print(" ")
        print(" ")
        Secuencia = BFSsearch(self)
        print("Leyenda: ")
        print("O = Obstaculo")
        print("C = Casilla")

        print(" ")
        print("Posicion inical del Agente: ", self.pos)
        print("Posicion del Objetivo: ", self.obj)
        print(" ")
        #Encontro secuencia
        if Secuencia != None:
            print("Recorrido del agente: ")
            print(Secuencia)
        #No encontro secuencia    
        else: 
            print("No hay camino valido hacia el objetivo")

def is_next(Est1, Est2):
    Resta = [Est1[0]-Est2[0],Est1[1]-Est2[1]]
    if Resta == [0,1] or Resta == [0,-1] or Resta == [1,0] or Resta == [-1,0]:
        return True
#Algoritmo de busqueda a lo ancho a travez de la grilla
def BFSsearch(self):
        while self.casillasFronteras.empty() != True:
            Estado = self.casillasFronteras.get()
            self.env.grilla[Estado[0]][Estado[1]] = "E"

            if Estado == self.obj:
                Lista = []
                Lista.append(Estado)
                return Lista
            else:     
                 #Chequea que los movimientos sean validos, en caso de serlos lo ingresa en la cola FIFO           
                if self.env.accept_action(Estado[0],Estado[1],'up'):
                    self.env.grilla[Estado[0]-1][Estado[1]] = "F"
                    self.casillasFronteras.put([Estado[0]-1,Estado[1]])

                if self.env.accept_action(Estado[0],Estado[1],'down'):
                    self.env.grilla[Estado[0]+1][Estado[1]] = "F"
                    self.casillasFronteras.put([Estado[0]+1,Estado[1]])

                if self.env.accept_action(Estado[0],Estado[1],'right'):
                    self.env.grilla[Estado[0]][Estado[1]+1] = "F"
                    self.casillasFronteras.put([Estado[0],Estado[1]+1])

                if self.env.accept_action(Estado[0],Estado[1],'left'):
                    self.env.grilla[Estado[0]][Estado[1]-1] = "F"
                    self.casillasFronteras.put([Estado[0],Estado[1]-1])

                Lista = BFSsearch(self)
                if Lista != None:
                    if is_next(Lista[0],Estado) == True:
                        Lista.insert(0,Estado)
                    return Lista

        return None
