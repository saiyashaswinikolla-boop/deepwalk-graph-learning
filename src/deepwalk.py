import pandas as pd

def load_graph(path):

    edges = pd.read_csv(path, sep=" ", header=None)
    edges.columns = ["node1", "node2"]

    graph = {}

    for _, row in edges.iterrows():

        u = row["node1"]
        v = row["node2"]

        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    return graph
