import random
import math

def create():
    liste=[]
    for i in range(5):
        liste.append (int(random.randint(20,50)))
    print(liste)
    for i in liste:
        if i%2==0:
            liste[liste.index(i)]=int(math.pow(i,2))
    print(liste)
        
create()            


