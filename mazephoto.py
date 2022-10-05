
from random import shuffle, randrange
from PIL import Image, ImageDraw
import time


def construire_labyrinthe(taille, nom):
    print("Start : %s" % time.ctime())
    visited = [[0] * taille + [1]
               for _ in range(taille)] + [[1] * (taille + 1)]
    ver = [[".."]+["#."] * (taille-1) + ['#']]+[["#."] * taille + ['#']
                                                for _ in range(taille-2)]+[["#."] * (taille) + ["."]] + [[]]
    hor = [[".#"]+["##"] * (taille-1) + ['#']]+[["##"] * taille + ['#']
                                                for _ in range(taille-1)] + [["#"] * (2*taille-1) + ['#.']]

    def Afficher():
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        print(s)

    def creer_liste_voisins(x, y):
        listevoisins = []
        for (xx, yy) in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if test_validite(xx, yy):
                listevoisins.append((xx, yy))
        shuffle(listevoisins)
        return listevoisins

    def test_validite(i, j):
        return (i >= 0 and i <= (taille-1)) and (j >= 0 and j <= (taille-1))

    def creer_labyrinthe(x, y):
        pile = []
        pile.append([x, y])
        while len(pile):
            coord = pile.pop()
            x = coord[0]
            y = coord[1]
            ListeVoisins = creer_liste_voisins(x, y)
            while len(ListeVoisins) > 0:
                (xx, yy) = ListeVoisins.pop(0)
                nouvelle_cellule = [xx, yy]
                if visited[xx][yy] != 1:
                    if xx == x:
                        hor[max(y, yy)][x] = "#."
                    if yy == y:
                        ver[y][max(x, xx)] = ".."
                    pile.append(nouvelle_cellule)
                    visited[xx][yy] = 1

    def ecrire_fichier_sortie(nom):
        s = ""
        ths = open(f"{nom}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        ths.write(s)
        ths.close()
 
    creer_labyrinthe(randrange(taille), randrange(taille))
    ecrire_fichier_sortie(nom)
    
    def createJPG():
        large = 3*(taille)
        img = Image.new('RGB', (large, large), (255, 255, 255))
        t = large//taille
        draw = ImageDraw.Draw(img)
        draw.line((large-1, 0, large-1, large-1), fill=(0, 0, 0), width=1)
        draw.line((0, large-2, large-1, large-1), fill=(0, 0, 0), width=1)
        draw.line((0, 0, large-1, 0), fill=(0, 0, 0), width=1)
        draw.line((0, 0, 0, large-1), fill=(0, 0, 0), width=1)

        for y in range(taille):
            for x in range(taille):
                try:
                    if ver[y][x] == "#.":
                        draw.line((t*x, t*y, t*x, t*y+t),
                                  fill=(0, 0, 0), width=1)
                    if hor[y][x] == "##":
                        draw.line((t*x, t*y, t*x+t, t*y),
                                  fill=(0, 0, 0), width=1)
                except:
                    pass
        img.show()
        img.save(f"{nom}.jpg")
    createJPG()

taille = int(input('Entrer la taille de maze: '))
nom = input('Entrer le nom de maze: ')
construire_labyrinthe(taille, nom)
print("End : %s" % time.ctime())