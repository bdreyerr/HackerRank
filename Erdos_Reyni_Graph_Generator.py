# Ben Dreyer
# Erdos Reyni Graph Generator
# 2.9.2020
# This file will generate a random graph
# Time complexity of this generator is unknown since it uses external library calls

import math
import os
import random
import re
import sys

from networkx.generators.random_graphs import erdos_renyi_graph

nodes = 10
probability = 0.4
graph = erdos_renyi_graph(nodes, probability)

print(graph.nodes)
print(graph.edges)

ar = [1, 5, 7, 3, 20, 5, 60, 20, 60]
print ar
ar.sort()
ar.append('#')
print ar