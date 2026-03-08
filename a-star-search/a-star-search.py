import heapq

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (h[start], start))  # (f_score, node)
    
    came_from = {}  # to reconstruct path
    g_score = {start: 0}  # cost from start to node
    f_score = {start: h[start]}  # estimated total cost

    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.insert(0, current)
            return path
        
        for neighbor, distance in graph[current].items():
            tentative_g = g_score[current] + distance
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    print("No path found")
    return []

if __name__ == "__main__":
    # Heuristic function
    h = {
        'A': 150, 'B': 100, 'C': 110, 'D': 30, 'E': 50,
        'F': 110, 'G': 140, 'H': 40, 'I': 35, 'J': 20, 'K': 0
    }

    # Graph with edge distances
    graph = {
        'A': {'G': 50, 'F': 25, 'C': 35, 'B': 70},
        'B': {'A': 70, 'D': 30},
        'C': {'A': 35, 'E': 15, 'D': 40},
        'D': {'B': 30, 'C': 40, 'E': 35, 'K': 30},
        'E': {'C': 15, 'F': 25, 'I': 15, 'K': 50, 'D': 35},
        'F': {'A': 25, 'G': 20, 'H': 20, 'I': 35, 'E': 25},
        'G': {'A': 50, 'F': 20, 'H': 35},
        'H': {'G': 35, 'F': 20, 'I': 10, 'K': 40, 'J': 35},
        'I': {'E': 15, 'F': 35, 'H': 10, 'K': 35},
        'J': {'H': 35, 'K': 20},
        'K': {'J': 20, 'H': 40, 'I': 35, 'E': 50, 'D': 30}
    }

    path = a_star('A', 'K')
    print("Best Path:", path)
