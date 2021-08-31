from random import*

#Clase el entorno para el algoritmo A*
class EnviromentA:
    def __init__(self):
        self.agentPos= [randint(0,99),randint(0,99)]
        self.objetivo= [randint(0,99),randint(0,99)]
        self.grilla = create_grilla(self)

    #Funcion para imprimir el entrono, al terminar, cambia todos los números a casillas para la impresion
    def print_enviroment(self):
        for i in range(100):
            for j in range(100):
              if type(self.grilla[i][j]) == int or self.grilla[i][j] == "F" or self.grilla[i][j] == "E":
                self.grilla[i][j] = "C"
        for i in range(100):
          print(self.grilla[i])

    def accept_action(self, Fil, Col, action):
        if action == "up":
            if Fil > 0 and type(self.grilla[Fil-1][Col]) == int:
                return True
            else:
                return False
        elif action == "down":
            if Fil < 99 and type(self.grilla[Fil+1][Col]) == int:
                return True
            else:
                return False
        elif action == "right":
            if Col < 99 and type(self.grilla[Fil][Col+1]) == int:
                return True
            else:
                return False
        elif action == "left":
            if Col > 0 and type(self.grilla[Fil][Col-1]) == int:
                return True
            else:
                return False

#Funcion para aproximar ladistancia desde un estado dado a el objetivo, resta ambos estado, luego suma los valores absolutos del resultado
# para calcular la minima distancia entre ambos estados, o en otras palabras la distancia en "linea recta"
def AproxDist(Env,Fil,Col):
    Obj = Env.objetivo
    resul = (abs(Obj[0]-Fil) + abs(Obj[1]-Col))
    return resul

#Crea la grilla calculando las aproximaciones de las distancias hacia el objetivo
def create_grilla(Env):
    Grilla = []
    for i in range (100):
        Lista = []
        for j in range (100):
            if random() <= 0.2:
                if [i,j] != Env.objetivo and [i,j] != Env.agentPos: 
                    Lista.append("O")
                else:
                    Lista.append(AproxDist(Env,i,j))
            else:
                Lista.append(AproxDist(Env,i,j))
        
        Grilla.append(Lista)
    return Grilla

