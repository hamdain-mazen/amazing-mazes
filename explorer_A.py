from maze_classes import *
import numpy as np

class Node(Cell):
    def __init__(self,maze,X,Y):
        
        self.cost = 0
        self.dist = 0
        self.heuristic = self.cost + self.dist

        self.X = X
        self.Y = Y

        self.walls = maze.maze_cells[X][Y].walls

        self.maze = maze
        self.symbol = self.maze.maze_cells[X][Y].symbol
        self.visited = self.maze.maze_cells[X][Y].visited

        self.parent = self.maze.maze_cells[0][0]

def dist(nod1,nod2):
    a = np.array((nod1.X, nod1.Y))
    b = np.array((nod2.X, nod2.Y))

    return np.linalg.norm(a-b)

def shorter_path(maze, start_nod, end_nod):
    maze.maze_cells[0][0].walls['W'] = True

    closedList = []
    openList = []
    
    # Adds START node to OPEN list
    start_nod.heuristic = dist(start_nod,end_nod)
    openList.append(start_nod)
    maze.maze_cells[start_nod.X][start_nod.Y].symbol = '*'
    
    while openList != []:
        
        # Priorise la liste par HEURISTIC 
        openList = sorted(openList, key=lambda node: node.heuristic)
        
        # Parcourt la liste triée
        for u in openList:
            
            # Si le premier noeud est le END, retourne la solution, retire le noeud et arrête le programme
            if u.X == end_nod.X and u.Y == end_nod.Y:
                build_path(u,maze,start_nod,end_nod)
                openList.remove(u)
            
            # Si le premier noeud n'est pas le END
            else:

                for v in neighbors(u):
                    v.dist = dist(v,end_nod)
                    v.cost = u.cost + 1
                    v.heuristic = v.dist + v.cost

                    in_open = False
                    in_closed = False

                    h_open = 0
                    h_closed = 0

                    for i in range(len(closedList)):
                        if v.X == closedList[i].X and v.Y == closedList[i].Y:
                            in_closed = True
                            h_closed = closedList[i].heuristic
                    
                    for i in range(len(openList)):
                        if v.X == openList[i].X and v.Y == openList[i].Y:
                            in_open = True
                            h_open = openList[i].heuristic
                    
                    if not ((in_open and h_open < v.heuristic) or (in_closed and h_closed < v.heuristic)):
                        v.cost = u.cost + 1 
                        v.heuristic = v.cost + dist(v, end_nod)
                        v.parent = u
                        openList.append(v)
                        maze.maze_cells[v.X][v.Y].symbol = '*'
                
                # Ajoute le noeud u à CLOSED et le retire de OPEN
                closedList.append(u)
                openList.remove(u)

    maze.maze_cells[0][0].walls['W'] = False

def build_path(nod,maze,start_nod,end_nod):
    while not ((nod.X == start_nod.X) and (nod.Y == start_nod.Y)):
        maze.maze_cells[nod.X][nod.Y].symbol = 'o'
        nod = nod.parent
    maze.maze_cells[nod.X][nod.Y].symbol = 'o'

def neighbors(nod):
    neighbors_ls =[]
    
    if nod.walls['N'] == False:
        neighbors_ls.append(Node(nod.maze,nod.X-1,nod.Y))

    if nod.walls['E'] == False:
        neighbors_ls.append(Node(nod.maze,nod.X,nod.Y+1))

    if nod.walls['S'] == False:
        neighbors_ls.append(Node(nod.maze,nod.X+1,nod.Y))

    if nod.walls['W'] == False:
        neighbors_ls.append(Node(nod.maze,nod.X,nod.Y-1))
    
    return neighbors_ls