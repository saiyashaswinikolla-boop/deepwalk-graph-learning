from load_graph import load_graph
from random_walk import random_walk

graph = load_graph("../data/facebook_combined.txt")

for node in list(graph.keys())[:5]:
    walk = random_walk(graph, node, 10)
    print(walk)
