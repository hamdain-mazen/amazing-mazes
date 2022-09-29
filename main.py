from premiere import *

#Crée un labyrinthe selon la taille saisie
# maze1 = Maze(int(input('Quelle taille de labybrinthe ?')))

#Affiche le labyrinthe dans la console
# maze1.Print()

#Ecrit le labyrinthe dans un fichier dont le nom est à saisir
# maze1.Write(input('Nom du fichier ?'))

# #Crée un labyrinthe de taille 6
maze1 = Maze(6)
maze1.Print()

#Choisit un cheminement de 3 cellules depuis la première et affiche leur index et leur état
# cell1 = Cellule(maze1, 1, 1)
# cell2 = cell1.Suiv()
# cell3 = cell2.Suiv()

# cell1.Print()
# cell2.Print()
# cell3.Print()

# chemin = []
# i = 0
# if i == 0:
#     cellule = Cellule(maze1, 1, 1)
#     chemin[i] = cellule.ID()
#     cellule.Visit()
#     i = i + 1
# else: