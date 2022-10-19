# Author: Calvin Atkeson
# Date: 11/15/21
# Purpose: Lab4 Vertex class

from cs1lib import *

class Vertex:
    # initial function
    # takes in the name, location
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacent = []

    # draws each vertex
    # takes in the r, g, b values
    def draw(self, r=0, g=0, b=1):
        set_fill_color(r, g, b)
        draw_circle(int(self.x), int(self.y), 5)

    # draws edges between vertices
    # takes in another vertex and the r, g, b values
    def draw_edge(self, adjacent_vertex, r=0, g=0, b=1):
        set_stroke_color(r, g, b)
        set_stroke_width(3)
        draw_line(int(self.x), int(self.y), int(adjacent_vertex.x), int(adjacent_vertex.y))
        adjacent_vertex.draw(r, g, b)

    # draws all the adjacent edges to a vertex
    # takes in the r, g, b values
    def draw_adjacent_edges(self, r=0, g=0, b=1):
        for vertex in self.adjacent:
            self.draw_edge(vertex, r, g, b)

    # detects if the mouse is over a vertex
    # takes in the x and y position of the mouse
    def mdetect(self, mx, my):
        if int(self.x) - 5 < mx < int(self.x) + 5 and int(self.y) - 5 < my < int(self.y) + 5:
            return True

    # prints out each vertex
    # no parameters
    def __str__(self):
        adjacencies = "Adjacent vertices: "
        i = 0
        for vertex in self.adjacent:
            i = i + 1
            if i == len(self.adjacent):
                adjacencies = adjacencies + vertex.name
            else:
                adjacencies = adjacencies + vertex.name + ", "
        return self.name + "; Location:" + str(self.x) + ", " + str(self.y) + "; " + adjacencies
