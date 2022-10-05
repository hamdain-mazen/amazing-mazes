from maze_classes import *
from generator_RBT import build_recursive
import time

#Crée les murs du labyrinthe selon la taille saisie
times = [10,100,150, 175, 200 , 250, 300,350, 400,450, 500]
times = [1000]
exe =[]

for t in times:
    start = time.time()
    maze1 = build_recursive(Maze(t))
    exe.append(round(time.time()-start,2))

    fichier = open('temps' + '.txt',"w")
    fichier.write(str(times) + '\n' + str(exe))