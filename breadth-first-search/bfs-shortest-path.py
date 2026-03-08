from collections import deque

def bfs_shortest_path(graph, start, target):
    queue = deque()
    visited = set()
    distance = {}

    queue.append(start)
    visited.add(start)
    distance[start] = 0

    while queue:
        current = queue.popleft()

        if current == target:
            return distance[current]

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    return None  # no path found

if __name__ == "__main__":
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(bfs_shortest_path(graph, 'A', 'F'))



"""
    BFS_shortest_path(start, target):
    queue = empty queue
    visited = empty set
    distance = map with default value infinity

    add start to queue
    visited.add(start)
    distance[start] = 0

    while queue is not empty:
        current = queue.pop_front()

        if current == target:
            return distance[current]

        for each neighbor of current:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1
                queue.push_back(neighbor)

    return "no path found"

"""