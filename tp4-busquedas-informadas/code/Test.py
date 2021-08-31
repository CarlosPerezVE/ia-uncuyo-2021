from AgentA import AgentA
from EnviromentA import EnviromentA
import sys

sys.setrecursionlimit(10000)

Entorno = EnviromentA()

Agent = AgentA(Entorno)
Agent.think() 