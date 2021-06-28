#!/usr/bin/python3
"""
This program generates a small maze.
Consider this as the source code, all future modification
will be after this
"""


path = 'p'
wall = 'w'
undefined_tile = 'u'
height = 15
width = 33
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
