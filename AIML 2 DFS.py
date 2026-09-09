graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [''],
    'F': ['I', 'J'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
}

def depth_first_search(graph, current_node, visited_nodes=None):
    if visited_nodes is None:
        visited_nodes = set()
    
    visited_nodes.add(current_node)
    print(current_node, end=" ")
    
    for adjacent in graph.get(current_node, []):
        if adjacent not in visited_nodes:
            depth_first_search(graph, adjacent, visited_nodes)

print("Following is the Depth-First Search:")
print("DFS Traversal Order:", end=" ")
depth_first_search(graph_data, 'A')