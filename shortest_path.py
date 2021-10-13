import sys
import data_utils as du
import dijkstra_heap
import bellman_ford

# TODO: After finishing csv data load, call Bellman-Ford and Dijkstra alg.
def main():
    data_path = sys.argv[1]
    graph = du.load_csv_to_graph(data_path)
    graph.print()

    # TODO: implementation of alg.
    # bellman_ford(graph)
    # dijkstra_heap(graph)

if __name__ == "__main__":
    main()