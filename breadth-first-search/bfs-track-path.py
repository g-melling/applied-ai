from collections import deque

def bfs_shortest_path(graph, start, target):
    queue = deque([start])
    visited = set([start])

    # Keeps track of how we reached each node
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == target:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()

            path_length = len(path) - 1  # number of edges
            return path_length, path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None, None  # no path found

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    length, path = bfs_shortest_path(graph, 'A', 'F')
    
    print("Path length:", length)
    print("Shortest path:", path)