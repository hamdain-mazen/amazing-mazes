#Amazing Mazes
# Recursive Backtrack
from maze_classes import *

def build_recursive(maze):

    path = []
    cell = maze.maze_cells[0][0]
    path.append(cell.ID())
    cell.Visit()

    while len(path) < maze.N * maze.N:
        prev_X = cell.X
        prev_Y = cell.Y
        cell = next(cell)
        
        if cell == 'END':
            i = -1
            while maze.maze_cells[path[i][0]][path[i][1]].available_dir() == []:
                i = i - 1
            
            prev_X = path[i][0]
            prev_Y = path[i][1]
            cell = next(maze.maze_cells[path[i][0]][path[i][1]])
        
        if cell.X == prev_X:
            if cell.Y > prev_Y:
                dir = 'W'
            else:
                dir = 'E'

        elif cell.Y == prev_Y:
            if cell.X > prev_X:
                dir = 'N'
            else:
                dir = 'S'

        path.append(cell.ID())
        cell.Visit()
        cell.break_wall(dir)
    
    return maze

def next(cell):

    next_list = cell.available_dir()
    if next_list != []:
        dir = random.choice(next_list)

        if dir == 'N' and cell.X > 0:
            return cell.maze.maze_cells[cell.X-1][cell.Y]

        elif dir == 'E' and cell.Y < cell.maze.N - 1:
            return cell.maze.maze_cells[cell.X][cell.Y+1]

        elif dir == 'S' and cell.X < cell.maze.N - 1:
            return cell.maze.maze_cells[cell.X+1][cell.Y]

        elif dir == 'W' and cell.Y > 0:
            return cell.maze.maze_cells[cell.X][cell.Y-1]

        else:
            return cell.Next()

    else:
        return 'END'