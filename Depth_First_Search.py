# Ben Dreyer
# Depth First Search
# 2.9.2020
# This file traverses a graph using DFS
# Time complexity of this generator is unknown since it uses external library calls
# Inspiration from GeeksforGeeks.com

from networkx.generators.random_graphs import erdos_renyi_graph

nodes = 10          # Edit this value for a specific number of nodes
probability = 0.4   # This value predicts the probability that each two nodes will have a connection, if set to 1,
                    # there will be nodes^2 edges
g = erdos_renyi_graph(nodes, probability)

print(g.nodes)
print(g.edges)

# We now have a randomly generated graph, below DFS is defiend to search it,
visited = [] # Empty list to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:                 # If the current node in graph has not been visited
        print node,                         # output that node
        visited.append(node)                # append that same node to visited list
        for neighbor in graph[node]:        # starting with an adjacent node to original node
            dfs(visited, graph, neighbor)   # recursively call dfs with neighbor node and updated visited
# Time complexity: O(n) where n is the number of nodes
# This implementation of DFS works for searching an traversing an array based on a given starting point
# How can I use this same implementation to search for a target node based on a starting point?

visited = []
def dfsTarget(visited, graph, nodeStart, nodeTarget):
    if nodeStart == nodeTarget:
        return True
    if nodeStart not in visited and nodeStart != nodeTarget:
        # print node,
        visited.append(nodeStart)
        for neighbor in graph[nodeTarget]:
            dfsTarget(visited, graph, neighbor, nodeTarget)
        if nodeTarget not in graph:
            return False
# Driver code
dfsTarget(visited, g, 0, 5)
print visited









