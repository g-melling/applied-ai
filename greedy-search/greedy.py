"""
Greedy-Best-First-Search(start, goal):

1. current ← start
2. path ← [current]

3. while current ≠ goal:
       among all neighbors of current
       choose neighbor n with minimum h(n)
       current ← n
       append current to path

4. return path
"""

def greedy(start, goal):
    current = start
    path = [current]
    
    while current != goal:
        neighbours = graph[current]
        if not neighbours:
            print("No path found")
            return path
        
        # Choose neighbour with minimum h(n)
        next_node = min(neighbours, key=lambda n: h[n])
        
        current = next_node
        path.append(current)
            
    return path


if __name__ == "main":
    
    # Define the heuristic function
    h = {
        'A': 150,
        'B': 100,
        'C': 110,
        'D': 30,
        'E': 50,
        'F': 110,
        'G': 140,
        'H': 40,
        'I': 35,
        'J': 20,
        'K': 0
    }

    # Define the graph (neighbours of each node)
    graph = {
        'A': ['G', 'F', 'C', 'B'],
        'B': ['A', 'D'],
        'C': ['A', 'E', 'D'],
        'D': ['B', 'C', 'E', 'K'],
        'E': ['C', 'F', 'I', 'K', 'D'],
        'F': ['A', 'G', 'H', 'I', 'E'],
        'G': ['A', 'F', 'H'],
        'H': ['G', 'F', 'I', 'K', 'J'],
        'I': ['E', 'F', 'H', 'K'],
        'J': ['H', 'K'],
        'K': ['J', 'H', 'I', 'E', 'D']
    }

    path = greedy('A', 'K')
    print("Best Path:", path)
    print("Length: ", (len(path) - 1))