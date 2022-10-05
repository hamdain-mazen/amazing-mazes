#Amazing Mazes
# Recursive Backtrack

def build_recursive(maze):

    path = []
    cell = maze.maze_cells[0][0]
    path.append(cell.ID())
    cell.Visit()

    while len(path) < maze.N * maze.N:
        prev_X = cell.X
        prev_Y = cell.Y
        cell = cell.Next()
        
        if cell == 'END':
            i = -1
            while maze.maze_cells[path[i][0]][path[i][1]].available_dir() == []:
                i = i - 1
            
            prev_X = path[i][0]
            prev_Y = path[i][1]
            cell = maze.maze_cells[path[i][0]][path[i][1]].Next()
        
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