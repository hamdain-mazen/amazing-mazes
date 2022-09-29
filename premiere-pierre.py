#Amazing Mazes
# Première pierre - Recursive Backtrack

def init_maze(n):
    maze = []

    for i in range(n*2+1):
        maze.append([])

        for j in range(n*2+1):
            maze[i].append([])
            if (i % 2) == 0:
                
                maze[i][j] = '#'
            else:
                if (j % 2) == 0:
                    maze[i][j] = '#'
                else:
                    maze[i][j] = '.'
    
    return maze

def str_maze(maze):
    
    maze_out = ''
    
    for i in range(len(maze)):

        if i != 0:
            maze_out = maze_out + '\n'

        for j in range(len(maze[i])):
            maze_out = maze_out + maze[i][j]
    
    return maze_out


def write_maze(maze,file_name):
    fichier = open(file_name + '.txt',"w")
    fichier.write(str_maze(maze))

maze1 = init_maze(int(input('Quelle taille de labybrinthe ?')))

print(str_maze(maze1))

write_maze(maze1,input('Nom du fichier ?'))