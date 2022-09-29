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
while END  == False:
    if i == 0:
        cell = Cell(maze1, 1, 1)
        path[i] = cell.ID()
        cell.Visit()
    
    else:
        cell = cell.Suiv()
        path[i] = cell.ID()
        cell.Visit()

    cell.Visit()
    i = i + 1