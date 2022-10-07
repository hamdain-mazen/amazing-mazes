from PIL import Image, ImageDraw

def createJPG(maze):
        size = maze.N
        large = 30 * size
        img = Image.new('RGB', (large, large), (255, 255, 255))
        t = large//size
        draw = ImageDraw.Draw(img)
        draw.line((0, 0, large-1, 0), fill=(0, 0, 0), width=10)
        draw.line((large-1, 0, large-1, large-1-t), fill=(0, 0, 0), width=10)
        draw.line((0, large-1, large-1, large-1), fill=(0, 0, 0), width=10)
        draw.line((0, t, 0, large-1), fill=(0, 0, 0), width=10)

        for I in range(size):
            for J in range(size):
                x = J
                y = I
                if maze.maze_cells[I][J].walls['S']:
                    draw.line((t*x, t*(y+1), t*(x+1), t*(y+1)), fill=(0, 0, 0), width=10)
                
                elif maze.maze_cells[I][J].symbol=='o' and maze.maze_cells[I+1][J].symbol=='o':
                    draw.line((t*x+t/2, t*y+t/2, t*x+t/2, t*(y+1)+t/2), fill=(0, 255, 0), width=10)
                
                if maze.maze_cells[I][J].walls['E']: 
                    draw.line((t*(x+1), t*y, t*(x+1), t*(y+1)), fill=(0, 0, 0), width=10)

                elif J != size-1 and maze.maze_cells[I][J].symbol=='o' and maze.maze_cells[I][J+1].symbol=='o':
                    draw.line((t*x+t/2, t*y+t/2, t*(x+1)+t/2, t*y+t/2), fill=(0, 255, 0), width=10)

                if maze.maze_cells[I][J].symbol=='*': 
                    draw.rectangle((t*(x+1/2)-t/6, t*(y+1/2)-t/6, t*(x+1/2)+t/6, t*(y+1/2)+t/6), fill=(255, 255, 0), width=10)

        img.show()
        img.save("TEST.jpg")