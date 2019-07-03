class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # removed the condition below--children wouldn't be added, because they wouldn't be in self.vertices
        # if v1 in self.vertices and v2 in self.vertices:
        self.vertices[v1].add(v2)

# graph terminology

# looks like depth first search--would be traversing the graph to the farthest away ancestor
# not technically distance, but does it relate more to the number of parents?
# 1. start with input value
# 2. locate the parents of the input value
# 3. locate parents of the parents, etc. etc
# 4. increment counts of parents
# 5. return parent after finding the max number of parents?

# build graph

# building graph using the parent child pairs

# traverse graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        # add edges!!!
    print(graph.vertices)

earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 1)