class Cell():
    def __init__(self,pos):
        self.pos = pos
        self.walls = {'N': True, 'S': True,'E': True,'W':True }

    def all_walls(self):
        if False not in self.walls.values():
            return True
        else:
            return False


    def break_the_walls(self, next_cell, wall):
        wall_sides = { 
                        'N': 'S'
                        'S': 'N'
                        'E':'W'
                        'W': 'E'
                        
                        }
        self.walls[wall] = False
        next_cell.walls[wall_sides[wall]] = False






# Here we gonna create the Maze class


class Maze:
    def __init__(self):
        self.size = int(input('Size of maze ?'))
        self.filename = input('Name of maze ? ')
        self.start = (0,0)
        self.maze = [Cell((i,j)) for j in range(0, self.size)]


def __str__(self):
    row_mazes = ['#', *((self.maze*2)+1)]
    for y in range(self.size):
        row_maze = ['#']
        for x in range(self.size):
            if self.maze[x][y].walls['E']:
                row_maze.append('.#')
            else:
                row_maze.append('..')
        row_mazes.append(''.join(row_maze))
        row_maze = ['#']
        for x in range(self.size):
            if self.maze[x][y].walls['S']:
                row_maze.append('##')
            else:
                row_maze.append('.#')
        row_mazes.append(''.join(row_maze))
    

    row_mazes[1] = row_mazes[1].replace('#', '',1)
    return '\n'.join(row_mazes)


def cell_in_position(self, pos):



    return self.maze[pos[0]][pos[1]]


def neighs(self, cell):
    



    