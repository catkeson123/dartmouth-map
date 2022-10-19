# Author: Calvin Atkeson
# Date: 11/15/21
# Purpose: Lab4 bfs search

from vertex import Vertex
from collections import deque

def bfs(start, goal):
    # dictionary for backpointers and queue of vertices
    backpointer = {}
    q = deque()

    backpointer[start] = None
    q.append(start)

    # bfs search
    while len(q) > 0:
        vertex = q.popleft()
        if vertex == goal:
            shortest_path = []
            while vertex is not None:
                shortest_path.append(vertex)
                vertex = backpointer[vertex]
            return shortest_path
        else:
            for a in vertex.adjacent:
                if a not in backpointer:
                    q.append(a)
                    backpointer[a] = vertex
    return None
