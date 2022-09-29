def readMaze(maze, filename):
    mazeFile = open(filename, "r")
    columns = mazeFile.readlines()
    for column in columns:
        column = column.strip()
        row = [i for i in column]
        maze.append(row)

maze =[]
readMaze(maze, "maze.txt")
#maze=[['.','.','.'],['#','#','.'],['.','.','.']]
H = len(maze)
L = len(maze[0])
print (maze[0][0])
print(maze[-1][-1])

def neighbors(i,j):
    global H,L
    tmp = [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
    neigh = []
    for k,l in tmp:
        if k >= 0 and k < H and l >= 0 and l < L :
            neigh.append((k,l))
    return neigh


def parcours(starti,startj,endi,endj):
    global maze,H,L
    file = [(starti,startj,starti,startj)]
    while file != []:
        i,j,previ,prevj = file.pop()
        if maze[i][j] == '#':
            None
        elif i == endi and j == endj:
            maze[i][j] = (previ,prevj)
            return 1
        elif maze[i][j] == '.' :
            maze[i][j] = (previ,prevj)
            for k,l in neighbors(i,j):
                file = [(k,l,i,j)] + file
    return 0

def replace_x(i,j):
    global maze
    if (i,j) == maze[i][j]:
        maze[i][j] = 'X'
    else:
        k,l = maze[i][j]
        maze[i][j] = 'X'
        replace_x(k,l)

def replace_dot():
    global maze
    for i in range(H):
        for j in range(L):
            if maze[i][j] not in ['X','#']:
                maze[i][j]='.'

print(parcours(0,0,H-1,L-1))
replace_x(H-1,L-1)
replace_dot()
print(maze)

with open('maze-out.txt','w') as f :
    for l in maze:
        f.write(''.join(l)+'\n')


