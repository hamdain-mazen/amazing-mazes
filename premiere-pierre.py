#Labyrinthe

#import numpy as np
#import re



maze = []
n = int(input('Quelle taille de labybrinthe ?'))

for i in range(n*2+1):
    maze.append([])
    print(maze)
    for j in range(n*2+1):
        maze[i].append([])
        if (i % 2) == 0:
            
            maze[i][j] = '#'
        else:
            if (j % 2) == 0:
                maze[i][j] = '#'
            else:
                maze[i][j] = '.'

print(maze)

fichier = open("output_maze.txt","w")
fichier.write(str(maze))

# pattern = '.'
# for i in range(ligne):
#     maze_col.append(re.findall(pattern,maze_lg[i]))
# # print('maze_col',maze_col)

# col = len(maze_col[0])

# #fonction qui teste la possibilité d'une position en fonction de la liste des positions des dames précédentes
# def possible(lgn,ls_pos):
#     if len(ls_pos) < 1:
#         return True
#     else:    
#         for i in range(len(ls_pos)):
#             diff_col = len(ls_pos) - i

#             if ls_pos[i] == lgn:
#                 return False
#             elif ls_pos[i] == lgn - diff_col:
#                 return False    
#             elif ls_pos[i] == lgn + diff_col:
#                 return False

#         return True

# # maze2d = np.array([])

# # for i in range(ligne):
# #     maze2d = np.append(maze2d, maze_lg[i])
# #     print('maze2d',maze2d,len(maze2d))
# #     for j in range(col):
# #         maze2d = np.append(maze2d, maze_lg[i], axis=0)
# #         print('maze2d',maze2d)
# # print('maze2d',maze2d)

# # #création classe Board pour visualiser les solutions
# # class Board:
# #     def __init__(self,n):
# #         self.plateau = np.zeros([n, n], dtype = str)
# #         for i in range(n):
# #             for j in range(n):
# #                 self.plateau[i,j] = 'O'
# #         self.taille = n

# #     def Print(self):
# #         print(self.plateau)

# #     def Visualiser(self,positions):
# #         for i in range(len(positions)):
# #             self.plateau[i,positions[i]] = 'X'



# #fonction de résolution en fonction de la taille du plateau
# def resolution(taille,col):
#     solutions = []

#     if col == 1:
#         for lig in range(taille):
#             solutions.append([lig])

#             if lig == taille - 1:
#                 return solutions
#     else:
#         solutions_i = resolution(taille,col-1)
#         len_i = len(solutions_i)

#         for sol in range(len_i):
#             for lig in range(taille):
#                 if possible(lig,solutions_i[sol]) == True:
#                     solutions.append(solutions_i[sol] + [lig])

#             if sol == len_i - 1:
#                 return solutions

# #fonction d'affichage du résultat
# def affichage(solutions):
#     if len(solutions) == 0:
#         print('Il n''y a pas de solutions',solutions)
#     else:
#         print('Il y a ' + str(len(solutions)) + ' solutions.','Les solutions sont :')
#         taille = len(solutions[0])
#         for i in range(len(solutions)):
#             resultat = Board(taille)
#             resultat.Visualiser(solutions[i])
#             print('\n' + 'Solution ' + str(i+1))
#             resultat.Print()

