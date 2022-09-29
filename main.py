from premiere import *

#Crée un labyrinthe selon la taille saisie

maze1 = Maze(int(input('Quelle taille de labybrinthe ?')))
# maze1.Print()

#Ecrit le labyrinthe dans un fichier dont le nom est à saisir
maze1.Write(input('Nom du fichier ?'))

#Crée un labyrinthe de taille 6
# maze1 = init_maze(6)
# print(str_maze(maze1))

#Choisit un cheminement de 3 cellules depuis la première et affiche leur index et leur état
# cell1 = Cellule(maze1, 1, 1)
# cell2 = cell1.Suiv()
# cell3 = cell2.Suiv()

# cell1.Print()
# cell2.Print()
# cell3.Print()