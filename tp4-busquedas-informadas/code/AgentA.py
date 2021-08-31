from PriorityQueue import*

#Clase agente para el algoritmo A*
class AgentA:
    def __init__(self, Enviroment):
        self.env = Enviroment
        self.pos = Enviroment.agentPos
        self.obj = Enviroment.objetivo
        self.front = []
        enqueue(self.front, self.pos, 0)
        self.env.grilla[self.pos[0]][self.pos[1]] = "F"

    #Funcion que calcula la secuencia de estados hacia el objetivo
    def think(self):
        Secuencia = AstarSearch(self, 0)
    
        print("Leyenda: ")
        print("O = Obstaculo")
        print("C = Casilla")
        self.env.print_enviroment()
        print("Posicion inicial del Agente: ", self.pos)
        print("Posicion del Objetivo: ", self.obj)
        print(Secuencia)
        if Secuencia != None:
            print("El largo de la secuencia es: ",len(Secuencia))

#funcion para selecionar los estados que pertenecen al la secuencia al salir de la recursividad
def is_next(Est1, Est2):
    Resta = [Est1[0]-Est2[0],Est1[1]-Est2[1]]
    if Resta == [0,1] or Resta == [0,-1] or Resta == [1,0] or Resta == [-1,0]:
        return True

#Funcion recursiva para la busqueda del algoritmo de A*, moviendose por los estados con aproximaciones menos costosas hasta
#llegar al objetivo
def AstarSearch(self, cont):

    while self.front != []:
        Estado = dequeue(self.front)
        self.env.grilla[Estado[0]][Estado[1]] = "E"

        if Estado == self.obj:
            Lista = []
            Lista.append(Estado)
            return Lista
        else:

            if self.env.accept_action(Estado[0], Estado[1], "up"):
                enqueue(self.front,[Estado[0]-1,Estado[1]],cont+self.env.grilla[Estado[0]-1][Estado[1]])
                self.env.grilla[Estado[0]-1][Estado[1]] = "F"

            if self.env.accept_action(Estado[0], Estado[1], "down"):
                enqueue(self.front,[Estado[0]+1,Estado[1]],cont+self.env.grilla[Estado[0]+1][Estado[1]])
                self.env.grilla[Estado[0]+1][Estado[1]] = "F"

            if self.env.accept_action(Estado[0], Estado[1], "right"):
                enqueue(self.front,[Estado[0],Estado[1]+1],cont+self.env.grilla[Estado[0]][Estado[1]+1])
                self.env.grilla[Estado[0]][Estado[1]+1] = "F"

            if self.env.accept_action(Estado[0], Estado[1], "left"):
                enqueue(self.front,[Estado[0],Estado[1]-1],cont+self.env.grilla[Estado[0]][Estado[1]-1])
                self.env.grilla[Estado[0]][Estado[1]-1] = "F"

            Lista = AstarSearch(self, cont+1)
            if Lista != None:
                if is_next(Lista[0],Estado) == True:
                    Lista.insert(0,Estado)
                return Lista

    return None