from graph import Graph
import time

"""
PSEUDOCODE:
Input:  Directed graph G = (V, E);
        edge lengths {le : e ∈ E} with no negative cycles;
        vertex s ∈ V
Output: For all vertices u reachable from s, dist(u) is set
        to the distance from s to u.

for all u ∈ V:
    dist(u) = ∞
    prev(u) = nil

dist(s) = 0

repeat |V| − 1 times:
    for all e ∈ E:
        update(e)

update((u, v) ∈ E)
    dist(v) = min{dist(v), dist(u) + l(u, v)}
"""

def bellman_ford(G: Graph, src: int):
    print('\nBellman-Ford start - Source node:', src)
    
    start_time = time.time()
    
    # Initialize array with ∞ cost
    distance = [float("Inf")] * G.total_nodes()
    
    # Initialize the predecessor array with null
    pred = [None] * G.total_nodes()
    
    # Set the cost of the src to itself as 0
    distance[src] = 0

    for _ in range(G.total_nodes() - 1):
        for edge in G.get_edges():
            [u, v, w] = edge.get_values()
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    pred[v] = u

    # Calculates the execution duration
    duration = round(time.time() - start_time, 10)

    # print('\nCosts:', distance)
    # print('Predecessors:', pred)
    # print('\nBellman-Ford end [Duration: {} seconds]'.format(duration))
    return [distance, pred, duration]