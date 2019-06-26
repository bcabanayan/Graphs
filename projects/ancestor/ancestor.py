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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
# looks like depth first search--would be traversing the graph to the farthest away ancestor
# not technically distance, but does it relate more to the number of parents?
# 1. start with input value
# 2. locate the parents of the input value
# 3. locate parents of the parents, etc. etc
# 4. increment counts of parents
# 5. return parent after finding the max number of parents?

