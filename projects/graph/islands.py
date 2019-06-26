from graph import Graph, Stack

def build_graph_from_matrix(islands):
    g = Graph()
    # traverse a 2d array....for loop for each row r...
    for r in range(len(islands)):
        # and for loop for each column c
        for c in range(len(islands[0])):
            # create a vertex for each 1 that you find; give it an id based on its absolute index
            if islands[r][c] == 1:
                index = len(islands) * r + c
                if index not in g.vertices.keys():
                    g.add_vertex(index)
                # check in each direction
                rn = r - 1
                rs = r + 1
                ce = c + 1
                cw = c - 1
                # check if index exists and if there is part of an island there
                if rn >= 0 and islands[rn][c] == 1:
                    n_index = len(islands) * rn + c
                    if n_index not in g.vertices.keys():
                        g.add_edge(index, n_index)
                # repeat for every direction....
    return g

def count_islands(islands):
    count = 0
    graph = build_graph_from_matrix(islands)
    my_vertices = dict(graph.vertices)
    visited = set()
    while len(my_vertices) > 0:
        neighbors = Stack()
        # setting vertex to key, and then adjacent neighbors to edges?
        vertex, edges = my_vertices.popitem()
        # check if already visited
        while vertex in visited:
            if len(my_vertices) == 0:
                return count
            else:
                vertex, edges = my_vertices.popitem()
        # add edges to stack
        neighbors.push(vertex)
        while neighbors.size() > 0:
            v = neighbors.pop()
            if v not in visited:
                visited.add(v)
                for neighbor in graph.vertices[v]:
                    neighbors.push(neighbor)
    return count

# strategy:
# 1. how does my graph translate in graph terminology
# 2. add graph/adjacency list
# 3. traverse the graph