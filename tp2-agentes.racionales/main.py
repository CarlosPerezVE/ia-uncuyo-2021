from Agent import Agent
from Environment import Environment

i=2
dirt_rate=0.8
print("---------------")
print("Dirt rate: "+ str(dirt_rate)+": ")
while i<=128:
    E= Environment(i,i,dirt_rate)
    A=Agent(E)
    A.think()
    print("==================")
    print("Performance "+str(i)+'x'+str(i)+': ')
    print(E.performance)
    print("==================")
    i=i*2    


