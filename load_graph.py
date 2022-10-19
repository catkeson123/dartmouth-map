# Author: Calvin Atkeson
# Date: 11/15/21
# Purpose: Lab4 load graph

from vertex import Vertex

# loads data in from the file
# takes in the file name
def load_graph(file_name):
    vertex_dict = {}

    file = open(file_name, "r")

    # create vertices with names and locations
    for line in file:
        # seperates each line by the semicolons
        line_list = line.strip().split(";")
        name = line_list[0]
        (x, y) = line_list[2].split(", ")
        # add each vertex to the dictionary
        vertex_dict[name] = Vertex(name, x, y)
    file.close()

    # add adjacent vertices to the vertices in the dictionary
    file = open(file_name, "r")
    for line in file:
        line_list = line.split(";")
        name = line_list[0]
        adjacent = line_list[1].split(",")
        for a in adjacent:
            vertex_dict[name].adjacent.append(vertex_dict[a.strip()])
    file.close()

    return vertex_dict
