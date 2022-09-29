#Amazing Mazes
# Première pierre - Recursive Backtrack

import random

class Maze:
    def __init__(self,n):
        self.n = n
        self.maze_matrix = []

        for i in range(n*2+1):
            self.maze_matrix.append([])

            for j in range(n*2+1):
                self.maze_matrix[i].append([])
                if (i % 2) == 0:
                    
                    self.maze_matrix[i][j] = '#'
                else:
                    if (j % 2) == 0:
                        self.maze_matrix[i][j] = '#'
                    else:
                        self.maze_matrix[i][j] = '.'

        self.maze_matrix[1][0] = '.'
        self.maze_matrix[-2][-1] = '.'

    def str_maze(self):
        
        maze_out = ''
        T = 2 * self.n + 1 
        for i in range(T):

            if i != 0:
                maze_out = maze_out + '\n'

            for j in range(T):
                maze_out = maze_out + self.maze_matrix[i][j]
        
        return maze_out

    def Print(self):
        print(self.str_maze())

    def Write(self,file_name):
        fichier = open(file_name + '.txt',"w")
        fichier.write(self.str_maze())

class Cellule:
    def __init__(self,maze,x,y):
        self.x = x
        self.y = y
        self.droite = maze[2 * self.x - 1][(2 * self.y - 1) + 1]
        self.gauche = maze[2 * self.x - 1][(2 * self.y - 1) - 1]
        self.haut = maze[(2 * self.x - 1) - 1][2 * self.y - 1]
        self.bas = maze[(2 * self.x - 1) + 1][2 * self.y - 1]
        self.maze = maze
        self.visited = False

    def Print(self):
        print('x',self.x,'y',self.y)
        print(' ' + self.haut)
        print(self.gauche + ' ' + self.droite)        
        print(' ' + self.bas)

    def Suiv(self):
        dir = random.randint(1,4)

        if dir == 1 and self.x > 1:
            return Cellule(self.maze,self.x-1,self.y)

        elif dir == 2 and self.y < len(self.maze)//2 :
            return Cellule(self.maze,self.x,self.y+1)

        elif dir == 3 and self.x < len(self.maze)//2 :
            return Cellule(self.maze,self.x+1,self.y)

        elif dir == 4 and self.y > 1:
            return Cellule(self.maze,self.x,self.y-1)
        
        return self.Suiv()