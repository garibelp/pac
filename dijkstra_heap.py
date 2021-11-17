import min_heap as mh
from graph import Graph
import data_utils as du
import time

"""
PSEUDOCODE:
Input:  Graph G = (V, E), directed or undirected;
        positive edge lengths {le : e ∈ E}; vertex s ∈ V
Output: For all vertices u reachable from s, dist(u) is set
        to the distance from s to u.

for all u ∈ V :
    dist(u) = ∞
    prev(u) = nil

dist(s) = 0

H = buildHeap(V)

while H is not empty:
    u = removeMinHeap(H)
    for all edges (u, v) ∈ E:
        if dist(v) > dist(u) + l(u, v):
            dist(v) = dist(u) + l(u, v)
            prev(v) = u
            updateHeap(H, v, dist(v))
"""


def dijkstra_heap(G: Graph, src: int):
    print('\nDijkstra with Heap start - Source node:', src)
    G.print()
    
    start_time = time.time()

    # Initialize array with ∞ cost
    distance = [float("Inf")] * G.total_nodes()

    # Initialize the predecessor array with null
    pred = [None] * G.total_nodes()

    # Set the cost of the src to itself as 0
    distance[src] = 0

    # Initialize the heap elements values
    heap_list = []
    pos_H = []
    for i in range(G.total_nodes()):
        heap_list.append(mh.HeapElement(distance[i], i))
        pos_H.append(i)
    
    heap_size = len(heap_list)

    # Replace source of heap and update position on pos_H
    du.switch_array_position(pos_H, 0, src)
    du.switch_array_position(heap_list, 0, src)

    # Initialize the heap
    while heap_size > 0:
        # First element on heap
        n, heap_size = mh.remove(heap_list, pos_H, heap_size)
        for edge in G.get_edges_to(n.content):
            [v, w, cost] = edge.get_values()
            if distance[v] != float("Inf") and distance[v] + cost < distance[w]:
                distance[w] = distance[v] + cost
                pred[w] = v
                # Implementation with update
                # mh.update(heap_list, pos_H, mh.HeapElement(distance[w], w))
                # Implementation with re-insertion
                heap_size = mh.insert(heap_list, pos_H, heap_size, mh.HeapElement(distance[w], w))
                
    # Calculates the execution duration
    duration = round(time.time() - start_time, 5)

    return [distance, pred, duration]