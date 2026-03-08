from collections import deque

def bfs(graph, start):
    queue = deque()
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        print(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    bfs(graph, 'A')
    
    
    """
    BFS(start_node):
    create an empty queue
    create an empty set called visited

    add start_node to queue
    mark start_node as visited

    while queue is not empty:
        current = remove front of queue
        process current

        for each neighbor of current:
            if neighbor is not visited:
                mark neighbor as visited
                add neighbor to queue

    """
