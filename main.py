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
while END  == False:
    if i == 0:
        cell = Cell(maze1, 1, 1)
        path.append(cell.ID())
        cell.Visit()
        i = i + 1
        print('\n')
        maze1.Print()
    
    else:
        cell = cell.Next()
        path.append(cell.ID())
        cell.Visit()
        i = i + 1
        print('\n')
        maze1.Print()