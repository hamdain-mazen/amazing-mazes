#Amazing Mazes
# Classes

import random

class Maze:
    def __init__(self,N):
        self.N = N

        self.maze_cells = []

        for I in range(N):
            self.maze_cells.append([])
            for J in range(N):
                self.maze_cells[I].append(Cell(self,I,J))
    
        self.maze_cells[0][0].walls['W'] = False
        self.maze_cells[N-1][N-1].walls['E'] = False

    def __str__(self):
        wall = {True:'#', False:'.'}
        
        maze_out = ''

        for I in range(self.N):
            
            maze_out_W = ''
            maze_out_C = ''

            for J in range(self.N):

                maze_out_W = maze_out_W + '#' + wall[self.maze_cells[I][J].walls['N']]
                maze_out_C = maze_out_C + wall[self.maze_cells[I][J].walls['W']] + self.maze_cells[I][J].symbol
            
            maze_out_W = maze_out_W + "#"
            maze_out_C = maze_out_C + wall[self.maze_cells[I][J].walls['E']]
            maze_out = maze_out + '\n' + maze_out_W + '\n' + maze_out_C

        maze_out_W = ''
        for J in range(self.N):
            maze_out_W = maze_out_W + '#' + wall[self.maze_cells[I][J].walls['S']]
        maze_out_W = maze_out_W + "#"
        
        maze_out = maze_out + '\n' + maze_out_W            

        return maze_out

    def Write(self,file_name):
        fichier = open(file_name + '.txt',"w")
        fichier.write(str(self))

class Cell:
    def __init__(self,maze,X,Y):
        self.X = X
        self.Y = Y

        self.walls = {
                        'N' : True,
                        'E' : True,
                        'W' : True,
                        'S' : True
                        }

        self.maze = maze
        self.symbol = '.'
        self.visited = False

    def __str__(self):
        wall = {True:'#', False:'.'}
        
        return ' ' + wall[self.walls['N']] + '\n' + wall[self.walls['W']] + self.symbol + wall[self.walls['E']] + '\n' + ' ' + wall[self.walls['S']]
    
    def ID(self):
        return [self.X, self.Y]

    def Visit(self):
        self.visited = True

    def walls_up(self):
        if False not in self.walls.values():
            return True
        else:
            return False

    def break_wall(self,dir):
        walls_pairs = {
                            'N' : 'S',
                            'S' : 'N',
                            'E' : 'W',
                            'W' : 'E'
                        }
        
        if dir == 'N':
            prev_X = self.X-1
            prev_Y = self.Y

        elif dir == 'E':
            prev_X = self.X
            prev_Y = self.Y+1

        elif dir == 'S':
            prev_X = self.X+1
            prev_Y = self.Y

        elif dir == 'W':
            prev_X = self.X
            prev_Y = self.Y-1

        self.walls[dir] = False
        self.maze.maze_cells[prev_X][prev_Y].walls[walls_pairs[dir]] = False

    def available_dir(self):
        dir_list = []
        if not (self.X == 0 or self.maze.maze_cells[self.X-1][self.Y].visited == True):
            dir_list.append('N')
        if not (self.Y == self.maze.N-1 or self.maze.maze_cells[self.X][self.Y+1].visited == True):
            dir_list.append('E')
        if not (self.X == self.maze.N-1 or self.maze.maze_cells[self.X+1][self.Y].visited == True):
            dir_list.append('S')
        if not (self.Y == 0 or self.maze.maze_cells[self.X][self.Y-1].visited == True):
            dir_list.append('W')
        return dir_list