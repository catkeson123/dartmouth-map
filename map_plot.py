# Author: Calvin Atkeson
# Date: 11/15/21
# Purpose: Lab4 Map plot

from cs1lib import *
from load_graph import *
from bfs import *

# load the map and create the dictionary of vertices
map = load_image("dartmouth_map.png")
vertices = load_graph("dartmouth_graph.txt")

# start and goal vertices
start = None
goal = None

# detects when a vertex is clicked by the mouse
# takes in the x and y position of the mouse
def mpressed(mx, my):
    global start
    start = None
    for vertex in vertices:
        if vertices[vertex].mdetect(mx, my):
            start = vertices[vertex]

# tracks current location of the mouse
# takes in the x and y location of the mouse
def mmove(mx, my):
    global goal
    if start is not None:
        for vertex in vertices:
            if vertices[vertex].mdetect(mx, my):
                goal = vertices[vertex]
    else:
        goal = None

# draws the map
# no parameters
def main():
    draw_image(map, 0, 0)
    old_vertex = goal

    for vertex in vertices:
        vertices[vertex].draw_adjacent_edges()

    if start is not None:
        start.draw(1, 0, 0)
        if goal is not None:
            goal.draw(1, 0, 0)
            # draws the shortest path
            shortest_path = bfs(start, goal)
            for vertex in shortest_path:
                vertex.draw_edge(old_vertex, 1, 0, 0)
                old_vertex = vertex


start_graphics(main, width=1012, height=811, mouse_press=mpressed, mouse_move=mmove)
