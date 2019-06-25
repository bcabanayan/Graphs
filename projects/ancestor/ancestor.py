
def earliest_ancestor(ancestors, starting_node):
# looks like depth first search--would be traversing the graph to the farthest away ancestor
# not technically distance, but does it relate more to the number of parents?
# 1. start with input value
# 2. locate the parents of the input value
# 3. locate parents of the parents, etc. etc
# 4. increment counts of parents
# 5. return parent after finding the max number of parents?