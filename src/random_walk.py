import random

def random_walk(graph, start, walk_length):

    walk = [start]
    current = start

    for _ in range(walk_length - 1):

        neighbors = graph[current]
        current = random.choice(neighbors)
        walk.append(current)

    return walk
