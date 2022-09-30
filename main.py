from premiere import *

#Crée un labyrinthe selon la taille saisie
# maze1 = Maze(int(input('Input maze size :')))

#Affiche le labyrinthe dans la console
# maze1.Print()

#Ecrit le labyrinthe dans un fichier dont le nom est à saisir
# maze1.Write(input('File name ?'))

# #Crée un labyrinthe de taille 6
maze1 = Maze(6)
maze1.Print()

#Choisit un cheminement de 3 cellules depuis la première et affiche leur index et leur état
# cell1 = Cell(maze1, 1, 1)
# cell2 = cell1.Next()
# cell3 = cell2.Next()

# cell1.Print()
# cell2.Print()
# cell3.Print()

path = []
i = 0
END = False
while i < 10:
    if i == 0:
        cell = Cell(maze1, 1, 1)
        path.append(cell.ID())
        cell.Visit()
        i = i + 1
        maze1.Print()
    
    else:
        cell = cell.Next()
        path.append(cell.ID())
        cell.Visit()
        maze1.Print()
        print(path)

        if cell.x == path[-2][0]:
            if cell.y > path[-2][1]:
                dir = 4
            else:
                dir = 2

        elif cell.y == path[-2][1]:
            if cell.x > path[-2][0]:
                dir = 1
            else:
                dir = 3

        if dir == 1:
            maze1.maze_matrix[cell.x-1][cell.y] = "|"

        elif dir == 2:
            maze1.maze_matrix[cell.x][cell.y+1] = "-"

        elif dir == 3:
            maze1.maze_matrix[cell.x+1][cell.y] = "|"

        elif dir == 4:
            maze1.maze_matrix[cell.x][cell.y-1] = "-"

        i = i + 1
        maze1.Print()