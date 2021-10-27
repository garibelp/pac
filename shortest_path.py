import sys
import data_utils as du
from dijkstra_heap import dijkstra_heap
from bellman_ford import bellman_ford

# TODO: After finishing csv data load, call Bellman-Ford and Dijkstra alg.
def main():
    execution_type = sys.argv[1]
    data_path = sys.argv[2]
    src_node = sys.argv[3]
    graph = du.load_csv_to_graph(data_path)

    if execution_type == 'b':    
        bellman_ford_info = bellman_ford(graph, int(src_node))
        print(bellman_ford_info)

    elif execution_type == 'd':
        dijkstra_heap_info = dijkstra_heap(graph, int(src_node))
        print(dijkstra_heap_info)
    
    else: print('No execution type provided (d or b)')

if __name__ == "__main__":
    main()