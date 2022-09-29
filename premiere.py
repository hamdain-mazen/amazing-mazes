#Amazing Mazes
# Première pierre - Recursive Backtrack

import random

class Maze:
    def __init__(self,N):
        self.N = N
        self.n = 2 * N + 1
        self.maze_matrix = []

        for i in range(self.n):
            self.maze_matrix.append([])

            for j in range(self.n):
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

        for i in range(self.n):
            if i != 0:
                maze_out = maze_out + '\n'


            for j in range(self.n):
                maze_out = maze_out + self.maze_matrix[i][j]

        return maze_out

    def Print(self):
        print(self.str_maze())


    def Write(self,file_name):
        fichier = open(file_name + '.txt',"w")
        fichier.write(self.str_maze())

class Cell:

    def __init__(self,maze,X,Y):
        self.X = X
        self.x = 2 * self.X - 1
        self.Y = Y
        self.y = 2 * self.Y - 1

        self.right = maze[x][y + 1]
        self.left = maze[x][y - 1]
        self.up = maze[x - 1][y]
        self.down = maze[x + 1][y]

        self.maze = maze
        self.visited = False

    def Print(self):

        print('X',self.X,'Y',self.Y)

        print(' ' + self.up)
        print(self.left + ' ' + self.right)
        print(' ' + self.down)
    
    def ID(self):
        return [self.X, self.Y]

    def Next(self):
        dir = random.randint(1,4)

        if dir == 1 and self.X > 1:
            return Cell(self.maze,self.X-1,self.Y)

        elif dir == 2 and self.Y < len(self.maze)//2 :
            return Cell(self.maze,self.X,self.Y+1)

        elif dir == 3 and self.X < len(self.maze)//2 :
            return Cell(self.maze,self.X+1,self.Y)

        elif dir == 4 and self.Y > 1:
            return Cell(self.maze,self.X,self.Y-1)

        return self.Next()

    def Visit(self):
        self.visited = True
        self.maze.maze_matrix[self.x, self.y] = '+'