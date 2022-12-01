'''Representation of dijkstra algorithm'''

graph = {
    'start': {'a': 5, 'b': 2},
    'a': {'c': 4, 'd': 2},
    'b': {'a': 8, 'd': 7},
    'c': {'fin': 3, 'd': 6},
    'd': {'fin': 1},
    'fin': {},
}

infinity = float("inf")
costs = {'a': 5, 'b': 2, 'c': infinity, 'd': infinity, 'fin': infinity}

parents = {
    'a': 'start',
    'b': 'start',
    'c': None,
    'd': None,
    'fin': None,
}

processed = []


def find_lowest_cost_node():
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def lowest_weight():
    node = find_lowest_cost_node()
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node()
    return costs['fin']


print(lowest_weight())
