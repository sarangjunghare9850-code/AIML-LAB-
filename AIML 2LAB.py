from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    all_nodes = set(graph.keys())
    for node_edges in graph.values():
        all_nodes.update(node_edges.keys())
    
    g_score = {node: float('inf') for node in all_nodes}
    g_score[start] = 0
    
    open_nodes = PriorityQueue()
    open_nodes.put((heuristic[start], start)) 
    
    previous_nodes = {}

    while not open_nodes.empty():
        current_f_score, current_node = open_nodes.get()
        
        if current_f_score > g_score[current_node] + heuristic[current_node]:
            continue

        if current_node == goal:
            path = [current_node]
            while current_node in previous_nodes:
                current_node = previous_nodes[current_node]
                path.insert(0, current_node)
            return path, g_score[goal] 

        for neighbor, distance in graph[current_node].items():
            temp_g_score = g_score[current_node] + distance
            
            if temp_g_score < g_score[neighbor]:
                g_score[neighbor] = temp_g_score
                total_estimated_cost = temp_g_score + heuristic[neighbor]
                open_nodes.put((total_estimated_cost, neighbor))
                previous_nodes[neighbor] = current_node
                
    return None, float('inf')

network = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 5, 'E': 3},
    'C': {'A': 4, 'F': 2},
    'D': {'B': 5, 'G': 3},
    'E': {'B': 3, 'G': 1},
    'F': {'C': 2, 'G': 6},
    'G': {'D': 3, 'E': 1, 'F': 6}
}

heuristic_to_g = {
    'A': 7,
    'B': 4,
    'C': 8,
    'D': 3,
    'E': 1,
    'F': 6,
    'G': 0
}

start_node = 'A'
goal_node = 'G'
path, cost = a_star_search(network, start_node, goal_node, heuristic_to_g)

if path:
    print(f"Path found from {start_node} to {goal_node}: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")