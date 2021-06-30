#!/usr/bin/python3
"""
This program generates a small maze.
unused
"""

import random

mazewall = "#"
mazepath = " "
empty_tile = "t"
widthlvl = [9, 15, 25, 35]
heightlvl = [15, 35, 55, 75]
maze = []


class MazeModel:
    """class to design maze size based on the """

    def __init__(self, gamelevel=0):
        """initialization of the maze level"""
        for lvl in range(4):
            if gamelevel == lvl:
                width = widthlvl[gamelevel]
                height = heightlvl[gamelevel]

    def emptyRoom(self, maze):
        """function to make undefined tiles with maze dimensions"""
        for row in range(self.__init__.height):
            line = []
            for column in range(width):
                if row == 0 or row == height - 1:
                    line.append(mazewall)
                elif column == 0 or column == width - 1:
                    line.append(mazewall)
                else:
                    line.append(empty_tile)
            maze.append(line)

    def pathMaker(maze):
        """function to make """



maze = init_maze(width, height)
print_maze(maze)
starting_height = int(random.random() * height)
starting_width = int(random.random() * width)
if starting_height == 0:
    starting_height += 1
if starting_height == height-1:
    starting_height -= 1
if starting_width == 0:
    starting_width += 1
if starting_width == width-1:
    starting_width -= 1
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height-1, starting_width])
walls.append([starting_height, starting_width-1])
walls.append([starting_height, starting_width+1])
walls.append([starting_height+1, starting_width])
maze[starting_height-1][starting_width] = wall
maze[starting_height][starting_width-1] = wall
maze[starting_height][starting_width+1] = wall
maze[starting_height+1][starting_width] = wall
create_maze()
make_walls(width, height)
create_entrance_exit(width, height)
print_maze(maze)
