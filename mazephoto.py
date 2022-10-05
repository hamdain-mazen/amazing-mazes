from random import shuffle, randrange
from PIL import Image, ImageDraw
import time

# We start by building our maze
def build_maze(size, name):
    print("Start : %s" % time.ctime())
    visited = [[0] * size + [1]
               for _ in range(size)] + [[1] * (size + 1)]
    ver = [[".."]+["#."] * (size-1) + ['#']]+[["#."] * size + ['#']
                                                for _ in range(size-2)]+[["#."] * (size) + ["."]] + [[]]
    hor = [[".#"]+["##"] * (size-1) + ['#']]+[["##"] * size + ['#']
                                                for _ in range(size-1)] + [["#"] * (2*size-1) + ['#.']]
    # we define a method to display our maze
    def Display():
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        print(s)
    

    # we create a list of neighbours

    def create_list_neigh(x,y):
    
        list_neighs = []
        for (xx, yy) in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if test_validity(xx, yy):
                list_neighs.append((xx, yy))
        shuffle(list_neighs)
        return list_neighs
    
    def test_validity(i, j):
        return (i >= 0 and i <= (size-1)) and (j >= 0 and j <= (size-1))

    def create_labyrinth(x, y):
        pile = []
        pile.append([x, y])
        while len(pile):
            coord = pile.pop()
            x = coord[0]
            y = coord[1]
            ListNeighs = create_list_neigh(x, y)
            while len(ListNeighs) > 0:
                (xx, yy) = ListNeighs.pop(0)
                new_cell = [xx, yy]
                if visited[xx][yy] != 1:
                    if xx == x:
                        hor[max(y, yy)][x] = "#."
                    if yy == y:
                        ver[y][max(x, xx)] = ".."
                    pile.append(new_cell)
                    visited[xx][yy] = 1

    def maze_output(nom):
        s = ""
        file = open(f"{name}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        file.write(s)
        file.close()

    create_labyrinth(randrange(size), randrange(size))
    maze_output(name)


    def createJPG():
        large = 3*(size)
        img = Image.new('RGB', (large, large), (255, 255, 255))
        t = large//size
        draw = ImageDraw.Draw(img)
        draw.line((large-1, 0, large-1, large-1), fill=(0, 0, 0), width=1)
        draw.line((0, large-2, large-1, large-1), fill=(0, 0, 0), width=1)
        draw.line((0, 0, large-1, 0), fill=(0, 0, 0), width=1)
        draw.line((0, 0, 0, large-1), fill=(0, 0, 0), width=1)

        for y in range(size):
            for x in range(size):
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
        img.save(f"{name}.jpg")
    createJPG()


size = int(input('Enter the size of the maze: '))
name = input('Enter the name of the maze: ')
build_maze(size, name)
print("End : %s" % time.ctime())    

