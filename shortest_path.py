import sys
import data_utils as du
import dijkstra_heap
from bellman_ford import bellman_ford

# TODO: After finishing csv data load, call Bellman-Ford and Dijkstra alg.
def main():
    data_path = sys.argv[1]
    src_node = sys.argv[2]
    graph = du.load_csv_to_graph(data_path)

    # TODO: implementation of alg.
    bellman_ford_info = bellman_ford(graph, int(src_node))
    print(bellman_ford_info)
    # dijkstra_heap(graph)

if __name__ == "__main__":
    main()